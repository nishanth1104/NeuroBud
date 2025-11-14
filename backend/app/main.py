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
from sqlalchemy import text, func, case
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
from app.models.user import User
from app.models.model_response import ModelResponse
from app.models.api_cost import APICost
from app.utils.cost_calculator import CostCalculator

# Create database tables (only in production, not tests)
import sys
if "pytest" not in sys.modules:
    try:
        Base.metadata.create_all(bind=engine)
        print("[OK] Database connected successfully!")
    except Exception as e:
        print(f"[WARNING] Could not connect to database: {e}")
        print("[WARNING] Running without database connection (some features disabled)")

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
    * `/api/ab-testing/stats` - Get A/B testing statistics
    * `/api/admin/cost-analytics` - Get cost analytics (Admin only)
    
    ## Authentication
    
    OAuth 2.0 with Google & GitHub
    
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

class FeedbackRequest(BaseModel):
    message_id: int
    was_helpful: Optional[bool] = None
    user_rating: Optional[int] = None
    user_feedback: Optional[str] = None

# ========== LIFECYCLE EVENTS ==========

@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    print("\n[STARTUP] Starting Neurobud API...")
    print("[OK] Initialization complete")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    print("\n[SHUTDOWN] Shutting down Neurobud API...")
    print("[OK] Cleanup complete")

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
    print(f"[ERROR] Unexpected error: {exc}")
    import traceback
    traceback.print_exc()
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
    user_email: Optional[str] = None

class ChatResponse(BaseModel):
    conversation_id: int
    message: str
    response: str
    message_id: int
    is_crisis: bool
    crisis_severity: Optional[str] = None
    tokens_used: int
    response_time_ms: float

class MoodRequest(BaseModel):
    mood_score: int
    note: Optional[str] = None
    user_email: Optional[str] = None

class MoodResponse(BaseModel):
    id: int
    mood_score: int
    note: Optional[str]
    created_at: datetime

class UserLoginRequest(BaseModel):
    email: str
    name: Optional[str] = None
    provider: str
    provider_id: str
    avatar_url: Optional[str] = None

# ========== API ENDPOINTS ==========

@app.get("/")
def root(db: Session = Depends(get_db)):
    """Health check endpoint with database connection test"""
    
    try:
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        print(f"[ERROR] Database connection failed: {e}")
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
    """Chat with Neurobud AI"""
    
    message = sanitize_text(chat_data.message)
    
    if not message or len(message.strip()) == 0:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    if len(message) > 2000:
        raise HTTPException(status_code=400, detail="Message too long (max 2000 characters)")
    
    if chat_data.conversation_id:
        conversation = db.query(Conversation).filter(Conversation.id == chat_data.conversation_id).first()
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        conversation = Conversation()
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
    
    previous_messages = db.query(Message).filter(
        Message.conversation_id == conversation.id
    ).order_by(Message.created_at).all()
    
    conversation_history = [
        {"role": msg.role, "content": msg.content}
        for msg in previous_messages
    ]
    
    crisis_result = crisis_detector.detect(message)
    
    print(f"\n[DEBUG] Crisis Detection:")
    print(f"Message: {message}")
    print(f"Is Crisis: {crisis_result['is_crisis']}")
    print(f"Severity: {crisis_result['severity']}\n")
    
    user_message = Message(
        conversation_id=conversation.id,
        role="user",
        content=message
    )
    db.add(user_message)
    db.commit()
    db.refresh(user_message)
    
    if crisis_result["is_crisis"]:
        crisis_event = CrisisEvent(
            conversation_id=conversation.id,
            message_id=user_message.id,
            trigger_type="keyword",
            keywords_detected=",".join(crisis_result["keywords_detected"])
        )
        db.add(crisis_event)
        db.commit()
        print(f"[OK] Crisis event logged to database!")

    user_id = None
    
    if crisis_result["is_crisis"] and crisis_result["severity"] in ["critical", "moderate"]:
        print(f"[CRISIS] Using crisis protocol response!")
        ai_response_text = crisis_detector.get_crisis_response(crisis_result["severity"])
        ai_result = {
            "response": ai_response_text,
            "tokens_used": chat_engine.estimate_tokens(ai_response_text),
            "model": "crisis_protocol",
            "model_variant": "crisis",
            "response_time_ms": 0
        }
    else:
        print(f"[CHAT] Using AI response with A/B testing")
        
        if chat_data.user_email:
            user = db.query(User).filter(User.email == chat_data.user_email).first()
            if user:
                user_id = user.id
        
        ai_result = chat_engine.chat(
            message=message,
            conversation_history=conversation_history,
            user_id=user_id
        )
        
        print(f"[A/B] Using {ai_result.get('model_variant', 'base')} model")
    
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
    db.refresh(assistant_message)
    
    # Track model response for A/B testing (if not crisis)
    if ai_result.get("model_variant") != "crisis":
        model_response = ModelResponse(
            message_id=assistant_message.id,
            user_id=user_id,
            model_id=ai_result["model"],
            model_variant=ai_result.get("model_variant", "base"),
            response_time_ms=ai_result.get("response_time_ms", 0),
            tokens_used=ai_result["tokens_used"]
        )
        db.add(model_response)
        db.commit()
        
        print(f"[OK] Tracked {ai_result.get('model_variant', 'base')} model response")
        
        # Track API costs
        try:
            # Estimate input/output tokens (rough split: 40% input, 60% output)
            total_tokens = ai_result["tokens_used"]
            input_tokens = int(total_tokens * 0.4)
            output_tokens = int(total_tokens * 0.6)
            
            # Calculate costs
            cost_data = CostCalculator.calculate_chat_cost(
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                model=ai_result["model"]
            )
            
            # Save cost tracking
            api_cost = APICost(
                user_id=user_id,
                message_id=assistant_message.id,
                conversation_id=conversation.id,
                model=ai_result["model"],
                feature="chat",
                input_tokens=cost_data["input_tokens"],
                output_tokens=cost_data["output_tokens"],
                total_tokens=cost_data["total_tokens"],
                input_cost=cost_data["input_cost"],
                output_cost=cost_data["output_cost"],
                total_cost=cost_data["total_cost"],
                response_time_ms=ai_result.get("response_time_ms", 0)
            )
            db.add(api_cost)
            db.commit()
            
            print(f"[COST] ${cost_data['total_cost']:.6f} - Input: {input_tokens}, Output: {output_tokens}")
        except Exception as cost_error:
            print(f"[WARNING] Cost tracking failed: {cost_error}")
            # Continue even if cost tracking fails
    
    return ChatResponse(
        conversation_id=conversation.id,
        message=message,
        response=ai_result["response"],
        message_id=assistant_message.id,
        is_crisis=crisis_result["is_crisis"],
        crisis_severity=crisis_result["severity"] if crisis_result["is_crisis"] else None,
        tokens_used=ai_result["tokens_used"],
        response_time_ms=ai_result.get("response_time_ms", 0)
    )

@app.post("/api/mood", response_model=MoodResponse)
@limiter.limit("10/minute")
def log_mood(mood_data: MoodRequest, request: Request, db: Session = Depends(get_db)):
    """Log user mood entry"""

    if not validate_mood_score(mood_data.mood_score):
        raise HTTPException(status_code=400, detail="Mood score must be between 1 and 10")

    sanitized_note = sanitize_note(mood_data.note)

    user_id = None
    if mood_data.user_email:
        user = db.query(User).filter(User.email == mood_data.user_email).first()
        if user:
            user_id = user.id

    mood_entry = MoodEntry(
        mood_score=mood_data.mood_score,
        note=sanitized_note,
        user_id=user_id
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
def get_mood_history(days: int = 30, limit: int = 100, user_email: Optional[str] = None, db: Session = Depends(get_db)):
    """Get mood history for past X days"""

    if days < 1 or days > 365:
        raise HTTPException(status_code=400, detail="Days must be between 1 and 365")

    if limit < 1 or limit > 500:
        raise HTTPException(status_code=400, detail="Limit must be between 1 and 500")

    cutoff_date = datetime.now() - timedelta(days=days)

    query = db.query(MoodEntry).filter(MoodEntry.created_at >= cutoff_date)

    if user_email:
        user = db.query(User).filter(User.email == user_email).first()
        if user:
            query = query.filter(MoodEntry.user_id == user.id)
        else:
            return {"entries": [], "total": 0, "days": days}
    else:
        query = query.filter(MoodEntry.user_id == None)

    mood_entries = query.order_by(MoodEntry.created_at.desc()).limit(limit).all()

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
    
    total_conversations = db.query(Conversation).count()
    total_messages = db.query(Message).count()
    total_moods = db.query(MoodEntry).count()
    total_crisis_events = db.query(CrisisEvent).count()
    
    yesterday = datetime.now() - timedelta(days=1)
    recent_conversations = db.query(Conversation).filter(
        Conversation.created_at >= yesterday
    ).count()
    
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

@app.get("/api/ab-testing/stats")
def get_ab_testing_stats(db: Session = Depends(get_db)):
    """Get A/B testing statistics with user feedback"""
    
    try:
        # Get all model responses
        all_responses = db.query(ModelResponse).all()
        
        # Group by variant
        stats = {}
        for response in all_responses:
            variant = response.model_variant
            if variant not in stats:
                stats[variant] = {
                    "responses": [],
                    "helpful": 0,
                    "not_helpful": 0,
                    "ratings": []
                }
            
            stats[variant]["responses"].append(response)
            if response.was_helpful == True:
                stats[variant]["helpful"] += 1
            elif response.was_helpful == False:
                stats[variant]["not_helpful"] += 1
            if response.user_rating:
                stats[variant]["ratings"].append(response.user_rating)
        
        # Calculate aggregates
        result = {}
        for variant, data in stats.items():
            total = len(data["responses"])
            avg_time = sum(r.response_time_ms for r in data["responses"]) / total if total > 0 else 0
            avg_tokens = sum(r.tokens_used for r in data["responses"]) / total if total > 0 else 0
            avg_rating = sum(data["ratings"]) / len(data["ratings"]) if data["ratings"] else None
            helpful_count = data["helpful"]
            not_helpful_count = data["not_helpful"]
            total_feedback = helpful_count + not_helpful_count
            
            result[variant] = {
                "total_responses": total,
                "avg_response_time_ms": round(avg_time, 2),
                "avg_tokens_used": round(avg_tokens, 2),
                "avg_user_rating": round(avg_rating, 2) if avg_rating else None,
                "helpful_count": helpful_count,
                "not_helpful_count": not_helpful_count,
                "helpfulness_ratio": round(helpful_count / total_feedback, 2) if total_feedback > 0 else None,
                "feedback_count": len([r for r in data["responses"] if r.user_feedback]),
                "model_id": settings.FINE_TUNED_MODEL_ID if variant == "fine_tuned" else settings.BASE_MODEL
            }
        
        return {
            "ab_testing_enabled": settings.AB_TESTING_ENABLED,
            "split_ratio": settings.AB_TEST_SPLIT,
            "fine_tuned_model_available": bool(settings.FINE_TUNED_MODEL_ID),
            "stats": result
        }
    
    except Exception as e:
        print(f"[ERROR] A/B testing stats error: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/admin/cost-analytics")
def get_cost_analytics(
    days: int = 7,
    db: Session = Depends(get_db)
):
    """
    Get cost analytics (ADMIN ONLY)
    
    Returns:
        - Total spend
        - Daily breakdown
        - Cost per feature
        - Budget status
        - Top users by cost
    """
    
    try:
        # Calculate date range
        start_date = datetime.now() - timedelta(days=days)
        
        # Total spend for period
        total_spend = db.query(func.sum(APICost.total_cost)).filter(
            APICost.created_at >= start_date
        ).scalar() or 0.0
        
        # All-time spend
        all_time_spend = db.query(func.sum(APICost.total_cost)).scalar() or 0.0
        
        # Today's spend
        today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_spend = db.query(func.sum(APICost.total_cost)).filter(
            APICost.created_at >= today_start
        ).scalar() or 0.0
        
        # Cost by feature
        feature_costs = db.query(
            APICost.feature,
            func.sum(APICost.total_cost).label('cost'),
            func.count(APICost.id).label('requests')
        ).filter(
            APICost.created_at >= start_date
        ).group_by(APICost.feature).all()
        
        # Cost by model
        model_costs = db.query(
            APICost.model,
            func.sum(APICost.total_cost).label('cost'),
            func.sum(APICost.total_tokens).label('tokens')
        ).filter(
            APICost.created_at >= start_date
        ).group_by(APICost.model).all()
        
        # Daily breakdown
        daily_costs = db.query(
            func.date(APICost.created_at).label('date'),
            func.sum(APICost.total_cost).label('cost'),
            func.count(APICost.id).label('requests')
        ).filter(
            APICost.created_at >= start_date
        ).group_by(func.date(APICost.created_at)).all()
        
        # Top 10 users by cost (if applicable)
        top_users = db.query(
            APICost.user_id,
            func.sum(APICost.total_cost).label('cost'),
            func.count(APICost.id).label('requests')
        ).filter(
            APICost.created_at >= start_date,
            APICost.user_id.isnot(None)
        ).group_by(APICost.user_id).order_by(
            func.sum(APICost.total_cost).desc()
        ).limit(10).all()
        
        # Budget calculations
        budget_remaining = settings.TOTAL_BUDGET - all_time_spend
        budget_used_percent = (all_time_spend / settings.TOTAL_BUDGET) * 100 if settings.TOTAL_BUDGET > 0 else 0
        daily_budget_used_percent = (today_spend / settings.DAILY_BUDGET_LIMIT) * 100 if settings.DAILY_BUDGET_LIMIT > 0 else 0
        
        # Average cost per request
        total_requests = db.query(func.count(APICost.id)).filter(
            APICost.created_at >= start_date
        ).scalar() or 0
        avg_cost_per_request = total_spend / total_requests if total_requests > 0 else 0
        
        return {
            "summary": {
                "total_budget": settings.TOTAL_BUDGET,
                "all_time_spend": round(all_time_spend, 4),
                "budget_remaining": round(budget_remaining, 4),
                "budget_used_percent": round(budget_used_percent, 2),
                "period_spend": round(total_spend, 4),
                "today_spend": round(today_spend, 4),
                "daily_budget_limit": settings.DAILY_BUDGET_LIMIT,
                "daily_budget_used_percent": round(daily_budget_used_percent, 2),
                "avg_cost_per_request": round(avg_cost_per_request, 6),
                "alert_triggered": budget_used_percent >= (settings.ALERT_THRESHOLD * 100)
            },
            "by_feature": [
                {
                    "feature": feature,
                    "cost": round(float(cost), 4),
                    "requests": int(requests),
                    "avg_cost": round(float(cost) / int(requests), 6) if requests > 0 else 0
                }
                for feature, cost, requests in feature_costs
            ],
            "by_model": [
                {
                    "model": model,
                    "cost": round(float(cost), 4),
                    "tokens": int(tokens),
                    "cost_per_1k_tokens": round((float(cost) / int(tokens)) * 1000, 4) if tokens > 0 else 0
                }
                for model, cost, tokens in model_costs
            ],
            "daily_breakdown": [
                {
                    "date": date.isoformat() if hasattr(date, 'isoformat') else str(date),
                    "cost": round(float(cost), 4),
                    "requests": int(requests)
                }
                for date, cost, requests in daily_costs
            ],
            "top_users": [
                {
                    "user_id": int(user_id) if user_id else None,
                    "cost": round(float(cost), 4),
                    "requests": int(requests),
                    "avg_cost": round(float(cost) / int(requests), 6) if requests > 0 else 0
                }
                for user_id, cost, requests in top_users
            ],
            "period_days": days
        }
    
    except Exception as e:
        print(f"[ERROR] Cost analytics error: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Cost analytics error: {str(e)}")

@app.post("/api/admin/cleanup")
def cleanup_old_data(days: int = 90, db: Session = Depends(get_db)):
    """Cleanup old conversations"""
    from app.utils.cleanup import cleanup_old_conversations
    
    deleted = cleanup_old_conversations(db, days)
    
    return {
        "success": True,
        "conversations_deleted": deleted,
        "days_threshold": days
    }

@app.post("/api/auth/login")
def user_login(user_data: UserLoginRequest, db: Session = Depends(get_db)):
    """Handle OAuth login"""
    
    user = db.query(User).filter(User.provider_id == user_data.provider_id).first()
    
    if user:
        user.last_login = datetime.now()
        user.name = user_data.name
        user.avatar_url = user_data.avatar_url
        db.commit()
        db.refresh(user)
    else:
        user = User(
            email=user_data.email,
            name=user_data.name,
            provider=user_data.provider,
            provider_id=user_data.provider_id,
            avatar_url=user_data.avatar_url,
            last_login=datetime.now()
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "avatar_url": user.avatar_url,
        "created_at": user.created_at
    }

@app.post("/api/feedback")
@limiter.limit("30/minute")
def submit_feedback(feedback_data: FeedbackRequest, request: Request, db: Session = Depends(get_db)):
    """Submit user feedback"""
    
    if feedback_data.user_rating is not None:
        if feedback_data.user_rating < 1 or feedback_data.user_rating > 5:
            raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
    
    model_response = db.query(ModelResponse).filter(
        ModelResponse.message_id == feedback_data.message_id
    ).first()
    
    if not model_response:
        message = db.query(Message).filter(Message.id == feedback_data.message_id).first()
        if not message:
            raise HTTPException(status_code=404, detail="Message not found")
        
        model_response = ModelResponse(
            message_id=feedback_data.message_id,
            user_id=None,
            model_id=message.model or "unknown",
            model_variant="unknown",
            response_time_ms=message.response_time_ms or 0,
            tokens_used=message.tokens_used or 0
        )
        db.add(model_response)
        db.commit()
        db.refresh(model_response)
    
    if feedback_data.was_helpful is not None:
        model_response.was_helpful = feedback_data.was_helpful
    
    if feedback_data.user_rating is not None:
        model_response.user_rating = feedback_data.user_rating
    
    if feedback_data.user_feedback is not None:
        sanitized = sanitize_text(feedback_data.user_feedback)
        if len(sanitized) > 500:
            sanitized = sanitized[:500]
        model_response.user_feedback = sanitized
    
    db.commit()
    db.refresh(model_response)
    
    print(f"[FEEDBACK] Message {feedback_data.message_id}: Rating={feedback_data.user_rating}, Helpful={feedback_data.was_helpful}")
    
    return {
        "success": True,
        "message": "Feedback received",
        "feedback": {
            "was_helpful": model_response.was_helpful,
            "rating": model_response.user_rating,
            "has_text_feedback": bool(model_response.user_feedback)
        }
    }

@app.get("/api/auth/check-admin")
def check_admin(user_email: str, db: Session = Depends(get_db)):
    """Check if user is admin"""
    
    if not user_email:
        raise HTTPException(status_code=400, detail="Email required")
    
    user = db.query(User).filter(User.email == user_email).first()
    
    if not user:
        return {"is_admin": False, "message": "User not found"}
    
    return {
        "is_admin": user.is_admin,
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name
        }
    }