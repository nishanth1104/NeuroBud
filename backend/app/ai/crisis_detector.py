from typing import Dict, List

class CrisisDetector:
    """Detect crisis situations in user messages"""
    
    # Crisis keywords organized by severity
    CRITICAL_KEYWORDS = [
        # Suicide-related (most specific first)
        "kill myself",
        "end my life", 
        "want to die",
        "don't want to live",
        "not want to live",
        "no reason to live",
        "better off dead",
        "suicide",
        "suicidal",
        "can't go on",
        "end it all",
        "not worth living",
        "goodbye forever",
        
        # Self-harm
        "cut myself",
        "hurt myself", 
        "self harm",
        "self-harm",
        "harm myself",
        
        # Immediate danger
        "going to hurt",
        "plan to die"
    ]
    
    MODERATE_KEYWORDS = [
        # Depression indicators
        "hopeless",
        "worthless",
        "can't take it",
        "give up",
        "no point",
        "nothing matters",
        "don't care anymore",
        
        # Despair
        "can't do this",
        "too much",
        "overwhelmed",
        "breaking point"
    ]
    
    def detect(self, message: str) -> Dict:
        """
        Detect crisis indicators in message
        
        Returns:
            {
                "is_crisis": bool,
                "severity": "none" | "moderate" | "critical",
                "keywords_detected": List[str],
                "recommended_action": str
            }
        """
        
        message_lower = message.lower().strip()
        detected_keywords = []
        
        # Check for critical keywords (check longer phrases first!)
        for keyword in self.CRITICAL_KEYWORDS:
            if keyword in message_lower:
                detected_keywords.append(keyword)
        
        if detected_keywords:
            print(f"[CRISIS-CRITICAL] Keywords found: {detected_keywords}")
            return {
                "is_crisis": True,
                "severity": "critical",
                "keywords_detected": detected_keywords,
                "recommended_action": "immediate_intervention"
            }

        # Check for moderate keywords
        for keyword in self.MODERATE_KEYWORDS:
            if keyword in message_lower:
                detected_keywords.append(keyword)

        if detected_keywords:
            print(f"[CRISIS-MODERATE] Keywords found: {detected_keywords}")
            return {
                "is_crisis": True,
                "severity": "moderate",
                "keywords_detected": detected_keywords,
                "recommended_action": "provide_resources"
            }
        
        # No crisis detected
        return {
            "is_crisis": False,
            "severity": "none",
            "keywords_detected": [],
            "recommended_action": "continue_conversation"
        }
    
    def get_crisis_response(self, severity: str) -> str:
        """Get appropriate crisis response based on severity"""
        
        if severity == "critical":
            return """URGENT: I'm really concerned about what you're sharing. Please reach out for immediate help:

**Call or text 988** - Suicide & Crisis Lifeline (24/7, free, confidential)
**Text HOME to 741741** - Crisis Text Line (24/7)
**Call 911** - If you're in immediate danger

You don't have to go through this alone. These are trained crisis counselors who can help right now. Will you reach out to one of them?"""
        
        elif severity == "moderate":
            return """I hear that you're going through a really difficult time. While I'm here to listen, what you're experiencing sounds like something that would really benefit from professional support.

**Resources that can help:**
- 988 Suicide & Crisis Lifeline: Call or text 988
- Crisis Text Line: Text HOME to 741741
- Find a therapist: https://www.psychologytoday.com/us/therapists

Would you like to talk about what's making things feel so overwhelming right now?"""
        
        else:
            return ""