import re
from typing import Optional

def sanitize_text(text: Optional[str], max_length: int = 2000) -> str:
    """
    Sanitize user input text.
    
    Args:
        text: Input text to sanitize
        max_length: Maximum allowed length
        
    Returns:
        Sanitized text
    """
    if not text:
        return ""
    
    # Remove null bytes
    text = text.replace('\x00', '')
    
    # Limit length
    text = text[:max_length]
    
    # Remove excessive whitespace
    text = ' '.join(text.split())
    
    # Remove potentially dangerous HTML/script tags
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<iframe[^>]*>.*?</iframe>', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    return text.strip()

def validate_mood_score(score: int) -> bool:
    """Validate mood score is in valid range."""
    return isinstance(score, int) and 1 <= score <= 10

def sanitize_note(note: Optional[str]) -> Optional[str]:
    """Sanitize mood note text."""
    if not note:
        return None
    
    sanitized = sanitize_text(note, max_length=500)
    return sanitized if sanitized else None