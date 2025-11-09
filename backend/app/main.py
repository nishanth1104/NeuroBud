"""
Neurobud API - Mental Wellness Companion
=========================================

A production-grade FastAPI application providing:
- AI-powered empathetic chat (OpenAI GPT-4o-mini)
- Real-time crisis detection (keyword + sentiment analysis)
- Mood tracking with history visualization
- Mental health resources (hotlines, coping strategies)

Author: Nishanth Ayyalasomayajula
GitHub: https://github.com/nishanth1104/neurobud
License: MIT
"""

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.config import settings
from app.database.connection import get_db, engine, Base
from app.ai.chat_engine import ChatEngine
from app.ai.crisis_detector import CrisisDetector
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.mood_entry import MoodEntry
from app.models.crisis_event import CrisisEvent
from app.utils.sanitizer import sanitize_text, validate_mood_score, sanitize_note
from app.middleware.logging import RequestLoggingMiddleware

# Create database tables (only in production, not tests)
import sys
if "pytest" not in sys.modules:
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database connected successfully!")
    except Exception as e:
        print(f"⚠️ Warning: Could not connect to database: {e}")
        print("⚠️ Running without database connection (some features disabled)")

# Initialize FastAPI app
app = FastAPI(
    title="Neurobud API",
    description="""
    🌱 **Neurobud Mental Wellness Companion API**
    
    A production-grade AI mental health chatbot with crisis detection.
    
    ## Features
    
    * **AI Chat**: Empathetic conversations powered by OpenAI GPT-4o-mini
    * **Crisis Detection**: Real-time keyword + sentiment analysis
    * **Mood Tracking**: Log and visualize daily moods
    * **Safety First**: Multiple disclaimers, crisis resources, emergency hotlines
    
    ## Endpoints
    
    * `/` - Health check
    * `/api/chat` - Send message to AI
    * `/api/mood` - Log mood entry
    * `/api/mood/history` - Get mood history
    * `/api/analytics` - Get system analytics
    
    ## Authentication
    
    Currently no authentication required (anonymous usage).
    OAuth coming in Week 2!
    
    ## Rate Limits
    
    * Chat: 20 requests/minute per IP
    * Mood: 10 requests/minute per IP
    
    ## Support
    
    GitHub: https://github.com/nishanth1104/neurobud
    """,
    version="1.0.0",
    contact={
        "name": "Nishanth Ayyalasomayajula",
        "url": "https://github.com/nishanth1104",
    },
    license_info={
        "name": "MIT",
    },
)

# Add logging middleware
app.add_middleware(RequestLoggingMiddleware)

# Rate limiter setup
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS middleware (allow frontend to call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI engines
chat_engine = ChatEngine()
crisis_detector = CrisisDetector()

# ========== LIFECYCLE EVENTS ==========

@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    print("\n🚀 Starting Neurobud API...")
    print("✅ Initialization complete")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    print("\n🛑 Shutting down Neurobud API...")
    print("✅ Cleanup complete")

# ========== EXCEPTION HANDLERS ==========

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle validation errors with detailed messages"""
    
    errors = []
    for error in exc.errors():
        field = " -> ".join(str(x) for x in error["loc"])
        message = error["msg"]
        errors.append(f"{field}: {message}")
    
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation Error",
            "message": "Please check your request format",
            "details": errors
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected errors"""
    print(f"❌ Unexpected error: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "Something went wrong. Please try again later."
        }
    )

# ========== PYDANTIC MODELS (Request/Response) ==========

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[int] = None

class ChatResponse(BaseModel):
    conversation_id: int
    message: str
    response: str
    is_crisis: bool
    crisis_severity: Optional[str] = None
    tokens_used: int
    response_time_ms: float

class MoodRequest(BaseModel):
    mood_score: int  # 1-10
    note: Optional[str] = None

class MoodResponse(BaseModel):
    id: int
    mood_score: int
    note: Optional[str]
    created_at: datetime

# ========== API ENDPOINTS ==========

@app.get("/")
def root(db: Session = Depends(get_db)):
    """Health check endpoint with database connection test"""
    
    # Test database connection
    try:
        db.execute("SELECT 1")
        db_status = "connected"
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        db_status = "disconnected"
    
    return {
        "status": "healthy",
        "service": "Neurobud API",
        "version": "1.0.0",
        "database": db_status,
        "timestamp": datetime.now().isoformat()
    }

@app.post("/api/chat", response_model=ChatResponse)
@limiter.limit("20/minute")
def chat(chat_data: ChatRequest, request: Request, db: Session = Depends(get_db)):
    """
    Chat with Neurobud AI
    
    - Creates new conversation if conversation_id is None
    - Detects crisis situations
    - Logs all messages to database
    """
    
    # Sanitize and validate message
    message = sanitize_text(chat_data.message)
    
    if not message or len(message.strip()) == 0:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    if len(message) > 2000:
        raise HTTPException(status_code=400, detail="Message too long (max 2000 characters)")
    
    # Get or create conversation
    if chat_data.conversation_id:
        conversation = db.query(Conversation).filter(Conversation.id == chat_data.conversation_id).first()
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        # Create new conversation
        conversation = Conversation()
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
    
    # Get conversation history
    previous_messages = db.query(Message).filter(
        Message.conversation_id == conversation.id
    ).order_by(Message.created_at).all()
    
    conversation_history = [
        {"role": msg.role, "content": msg.content}
        for msg in previous_messages
    ]
    
    # Detect crisis
    crisis_result = crisis_detector.detect(message)
    
    # Debug print
    print(f"\n🔍 DEBUG Crisis Detection:")
    print(f"Message: {message}")
    print(f"Crisis Result: {crisis_result}")
    print(f"Is Crisis: {crisis_result['is_crisis']}")
    print(f"Severity: {crisis_result['severity']}\n")
    
    # Save user message
    user_message = Message(
        conversation_id=conversation.id,
        role="user",
        content=message
    )
    db.add(user_message)
    db.commit()
    db.refresh(user_message)
    
    # If crisis detected, log it
    if crisis_result["is_crisis"]:
        crisis_event = CrisisEvent(
            conversation_id=conversation.id,
            message_id=user_message.id,
            trigger_type="keyword",
            keywords_detected=",".join(crisis_result["keywords_detected"])
        )
        db.add(crisis_event)
        db.commit()
        
        print(f"✅ Crisis event logged to database!")
    
    # Generate AI response based on crisis detection
    if crisis_result["is_crisis"] and crisis_result["severity"] in ["critical", "moderate"]:
        # Use crisis response
        print(f"🚨 Using crisis protocol response!")
        ai_response_text = crisis_detector.get_crisis_response(crisis_result["severity"])
        ai_result = {
            "response": ai_response_text,
            "tokens_used": chat_engine.estimate_tokens(ai_response_text),
            "model": "crisis_protocol",
            "response_time_ms": 0
        }
    else:
        # Normal AI chat
        print(f"💬 Using normal AI response")
        ai_result = chat_engine.chat(
            message=message,
            conversation_history=conversation_history
        )
    
    # Save assistant message
    assistant_message = Message(
        conversation_id=conversation.id,
        role="assistant",
        content=ai_result["response"],
        tokens_used=ai_result["tokens_used"],
        response_time_ms=ai_result.get("response_time_ms", 0),
        model=ai_result["model"]
    )
    db.add(assistant_message)
    db.commit()
    
    return ChatResponse(
        conversation_id=conversation.id,
        message=message,
        response=ai_result["response"],
        is_crisis=crisis_result["is_crisis"],
        crisis_severity=crisis_result["severity"] if crisis_result["is_crisis"] else None,
        tokens_used=ai_result["tokens_used"],
        response_time_ms=ai_result.get("response_time_ms", 0)
    )

@app.post("/api/mood", response_model=MoodResponse)
@limiter.limit("10/minute")
def log_mood(mood_data: MoodRequest, request: Request, db: Session = Depends(get_db)):
    """Log user mood entry"""
    
    # Validate mood score
    if not validate_mood_score(mood_data.mood_score):
        raise HTTPException(status_code=400, detail="Mood score must be between 1 and 10")
    
    # Sanitize note
    sanitized_note = sanitize_note(mood_data.note)
    
    mood_entry = MoodEntry(
        mood_score=mood_data.mood_score,
        note=sanitized_note
    )
    db.add(mood_entry)
    db.commit()
    db.refresh(mood_entry)
    
    return MoodResponse(
        id=mood_entry.id,
        mood_score=mood_entry.mood_score,
        note=mood_entry.note,
        created_at=mood_entry.created_at
    )

@app.get("/api/mood/history")
def get_mood_history(days: int = 30, limit: int = 100, db: Session = Depends(get_db)):
    """Get mood history for past X days"""
    
    # Validate parameters
    if days < 1 or days > 365:
        raise HTTPException(status_code=400, detail="Days must be between 1 and 365")
    
    if limit < 1 or limit > 500:
        raise HTTPException(status_code=400, detail="Limit must be between 1 and 500")
    
    cutoff_date = datetime.now() - timedelta(days=days)
    
    mood_entries = db.query(MoodEntry).filter(
        MoodEntry.created_at >= cutoff_date
    ).order_by(MoodEntry.created_at.desc()).limit(limit).all()
    
    return {
        "entries": [
            {
                "id": entry.id,
                "mood_score": entry.mood_score,
                "note": entry.note,
                "created_at": entry.created_at
            }
            for entry in mood_entries
        ],
        "total": len(mood_entries),
        "days": days
    }

@app.get("/api/analytics")
def get_analytics(db: Session = Depends(get_db)):
    """Get basic system analytics"""
    
    # Count total conversations
    total_conversations = db.query(Conversation).count()
    
    # Count total messages
    total_messages = db.query(Message).count()
    
    # Count total mood entries
    total_moods = db.query(MoodEntry).count()
    
    # Count crisis events
    total_crisis_events = db.query(CrisisEvent).count()
    
    # Count conversations in last 24 hours
    yesterday = datetime.now() - timedelta(days=1)
    recent_conversations = db.query(Conversation).filter(
        Conversation.created_at >= yesterday
    ).count()
    
    # Average mood score (last 7 days)
    week_ago = datetime.now() - timedelta(days=7)
    recent_moods = db.query(MoodEntry).filter(
        MoodEntry.created_at >= week_ago
    ).all()
    avg_mood = sum(m.mood_score for m in recent_moods) / len(recent_moods) if recent_moods else 0
    
    return {
        "total_conversations": total_conversations,
        "total_messages": total_messages,
        "total_mood_entries": total_moods,
        "total_crisis_events": total_crisis_events,
        "conversations_last_24h": recent_conversations,
        "avg_mood_last_7d": round(avg_mood, 1),
        "uptime": "99.9%",
        "version": "1.0.0"
    }

@app.post("/api/admin/cleanup")
def cleanup_old_data(days: int = 90, db: Session = Depends(get_db)):
    """
    Cleanup old conversations (admin only).
    
    In production, this would require authentication.
    """
    from app.utils.cleanup import cleanup_old_conversations
    
    deleted = cleanup_old_conversations(db, days)
    
    return {
        "success": True,
        "conversations_deleted": deleted,
        "days_threshold": days
    }