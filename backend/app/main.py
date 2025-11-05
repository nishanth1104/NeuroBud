from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session

from app.config import settings
from app.database.connection import get_db, engine, Base
from app.ai.chat_engine import ChatEngine
from app.ai.crisis_detector import CrisisDetector
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.mood_entry import MoodEntry
from app.models.crisis_event import CrisisEvent

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Neurobud API",
    description="Mental wellness companion API",
    version="1.0.0"
)

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
def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Neurobud API",
        "version": "1.0.0"
    }

@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    """
    Chat with Neurobud AI
    
    - Creates new conversation if conversation_id is None
    - Detects crisis situations
    - Logs all messages to database
    """
    
    # Get or create conversation
    if request.conversation_id:
        conversation = db.query(Conversation).filter(Conversation.id == request.conversation_id).first()
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
    crisis_result = crisis_detector.detect(request.message)
    
    # Save user message
    user_message = Message(
        conversation_id=conversation.id,
        role="user",
        content=request.message
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
    
    # Generate AI response
    if crisis_result["severity"] in ["critical", "moderate"]:
        # Use crisis response
        ai_response_text = crisis_detector.get_crisis_response(crisis_result["severity"])
        ai_result = {
            "response": ai_response_text,
            "tokens_used": chat_engine.estimate_tokens(ai_response_text),
            "model": "crisis_protocol",
            "response_time_ms": 0
        }
    else:
        # Normal AI chat
        ai_result = chat_engine.chat(
            message=request.message,
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
        message=request.message,
        response=ai_result["response"],
        is_crisis=crisis_result["is_crisis"],
        crisis_severity=crisis_result["severity"] if crisis_result["is_crisis"] else None,
        tokens_used=ai_result["tokens_used"],
        response_time_ms=ai_result.get("response_time_ms", 0)
    )

@app.post("/api/mood", response_model=MoodResponse)
def log_mood(request: MoodRequest, db: Session = Depends(get_db)):
    """Log user mood entry"""
    
    if request.mood_score < 1 or request.mood_score > 10:
        raise HTTPException(status_code=400, detail="Mood score must be between 1 and 10")
    
    mood_entry = MoodEntry(
        mood_score=request.mood_score,
        note=request.note
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
def get_mood_history(days: int = 30, db: Session = Depends(get_db)):
    """Get mood history for past X days"""
    
    from datetime import timedelta
    cutoff_date = datetime.now() - timedelta(days=days)
    
    mood_entries = db.query(MoodEntry).filter(
        MoodEntry.created_at >= cutoff_date
    ).order_by(MoodEntry.created_at.desc()).all()
    
    return {
        "entries": [
            {
                "id": entry.id,
                "mood_score": entry.mood_score,
                "note": entry.note,
                "created_at": entry.created_at
            }
            for entry in mood_entries
        ]
    }

# Run with: uvicorn app.main:app --reload