from sqlalchemy import Column, Integer, DateTime, Text
from sqlalchemy.sql import func
from app.database.connection import Base

class MoodEntry(Base):
    """User mood tracking entry"""
    __tablename__ = "mood_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    mood_score = Column(Integer, nullable=False)
    note = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<MoodEntry {self.id}: {self.mood_score}/10>"