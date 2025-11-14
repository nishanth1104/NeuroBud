from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey, Text
from sqlalchemy.sql import func
from app.database.connection import Base

class ModelResponse(Base):
    """Track A/B testing model responses"""
    __tablename__ = "model_responses"
    
    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer, ForeignKey("messages.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Model info
    model_id = Column(String, nullable=False)  # e.g., "gpt-4o-mini"
    model_variant = Column(String, nullable=False)  # "base" or "fine_tuned"
    
    # Performance metrics
    response_time_ms = Column(Float, nullable=False)
    tokens_used = Column(Integer, nullable=False)
    
    # User feedback (optional)
    user_rating = Column(Integer, nullable=True)  # 1-5 stars
    user_feedback = Column(Text, nullable=True)
    was_helpful = Column(Boolean, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<ModelResponse {self.id} - {self.model_variant}>"