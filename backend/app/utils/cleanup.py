from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.conversation import Conversation
from app.models.message import Message

def cleanup_old_conversations(db: Session, days: int = 90):
    """
    Delete conversations older than X days.
    
    Args:
        db: Database session
        days: Delete conversations older than this
        
    Returns:
        Number of conversations deleted
    """
    cutoff_date = datetime.now() - timedelta(days=days)
    
    # Find old conversations
    old_convs = db.query(Conversation).filter(
        Conversation.created_at < cutoff_date
    ).all()
    
    count = len(old_convs)
    
    # Delete associated messages first (if not cascading)
    for conv in old_convs:
        db.query(Message).filter(Message.conversation_id == conv.id).delete()
    
    # Delete conversations
    db.query(Conversation).filter(
        Conversation.created_at < cutoff_date
    ).delete()
    
    db.commit()
    
    return count