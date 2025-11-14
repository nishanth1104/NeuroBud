from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.connection import Base

class APICost(Base):
    """Track API costs per request"""
    __tablename__ = "api_costs"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Request info
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    message_id = Column(Integer, ForeignKey("messages.id"), nullable=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=True)
    
    # Model info
    model = Column(String, nullable=False)  # gpt-4o-mini, fine-tuned, etc.
    feature = Column(String, nullable=False)  # chat, embedding, sentiment, etc.
    
    # Token usage
    input_tokens = Column(Integer, default=0)
    output_tokens = Column(Integer, default=0)
    total_tokens = Column(Integer, default=0)
    
    # Cost breakdown (in USD)
    input_cost = Column(Float, default=0.0)
    output_cost = Column(Float, default=0.0)
    total_cost = Column(Float, default=0.0)
    
    # Metadata
    response_time_ms = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<APICost {self.id} - ${self.total_cost:.4f}>"