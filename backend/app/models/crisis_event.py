from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from app.database.connection import Base

class CrisisEvent(Base):
    """Logged crisis detection events"""
    __tablename__ = "crisis_events"
    
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)
    message_id = Column(Integer, ForeignKey("messages.id"), nullable=False)
    trigger_type = Column(String, nullable=False)
    keywords_detected = Column(Text, nullable=True)
    sentiment_score = Column(Integer, nullable=True)
    flagged_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<CrisisEvent {self.id} - {self.trigger_type}>"