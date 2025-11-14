import openai
import time
import random
from typing import List, Dict
from app.config import settings

class ChatEngine:
    """OpenAI chat engine with A/B testing support"""
    
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
        self.base_model = settings.BASE_MODEL
        self.fine_tuned_model = settings.FINE_TUNED_MODEL_ID
        self.ab_testing_enabled = settings.AB_TESTING_ENABLED
        self.ab_test_split = settings.AB_TEST_SPLIT
    
    def select_model(self, user_id: int = None) -> tuple[str, str]:
        """
        Select which model to use based on A/B testing
        
        Returns:
            (model_id, model_variant) tuple
            model_variant: 'base' or 'fine_tuned'
        """
        
        # If A/B testing disabled, use base model
        if not self.ab_testing_enabled:
            return (self.base_model, "base")
        
        # If no fine-tuned model, use base
        if not self.fine_tuned_model:
            return (self.base_model, "base")
        
        # If user_id provided, use consistent assignment
        if user_id:
            # Hash user_id to get consistent A/B assignment
            assignment = hash(user_id) % 100
            if assignment < (self.ab_test_split * 100):
                return (self.base_model, "base")
            else:
                return (self.fine_tuned_model, "fine_tuned")
        
        # Random assignment for guests
        if random.random() < self.ab_test_split:
            return (self.base_model, "base")
        else:
            return (self.fine_tuned_model, "fine_tuned")
    
    def chat(
        self, 
        message: str, 
        conversation_history: List[Dict] = None,
        user_id: int = None
    ) -> Dict:
        """
        Send message to OpenAI and get response
        
        Args:
            message: User's message
            conversation_history: Previous messages in conversation
            user_id: User ID for consistent A/B assignment
            
        Returns:
            Dict with response, tokens_used, model, variant, response_time_ms
        """
        
        start_time = time.time()
        
        # Select model (A/B testing)
        model_id, model_variant = self.select_model(user_id)
        
        # Prepare messages
        messages = [
    {
        "role": "system",
        "content": """You are Neurobud, an empathetic AI mental wellness companion specifically designed for mental health support.

IMPORTANT BOUNDARIES:
- You ONLY discuss mental health, emotional wellbeing, stress, anxiety, mood, and related wellness topics
- If asked about unrelated topics (math, general knowledge, coding, etc.), politely redirect to mental health
- Example: "I'm specifically designed to support mental wellness. Is there something about your emotional wellbeing or mental health I can help with?"

You provide:
- Emotional support and active listening
- Evidence-based coping strategies (CBT, mindfulness, breathing exercises)
- Validation and empathy without judgment
- Gentle guidance toward professional help when appropriate

You do NOT:
- Diagnose mental health conditions
- Prescribe medication or treatment
- Replace professional therapy
- Answer questions unrelated to mental health
- Make promises you can't keep

For crisis situations (self-harm, suicide ideation):
- Take them seriously and show concern
- Recommend immediate help (988 Suicide Lifeline, emergency services)
- Don't try to be a therapist

Your tone is warm, understanding, and human-like. You stay focused on mental wellness."""
    }
]
        
        # Add conversation history
        if conversation_history:
            messages.extend(conversation_history[-10:])  # Last 10 messages for context
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        try:
            # Call OpenAI
            response = openai.chat.completions.create(
                model=model_id,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            # Calculate metrics
            response_time_ms = (time.time() - start_time) * 1000
            
            return {
                "response": response.choices[0].message.content,
                "tokens_used": response.usage.total_tokens,
                "model": model_id,
                "model_variant": model_variant,  # 'base' or 'fine_tuned'
                "response_time_ms": response_time_ms
            }
            
        except Exception as e:
            print(f"OpenAI API error: {e}")
            raise
    
    def estimate_tokens(self, text: str) -> int:
        """Rough estimation of tokens (4 chars ≈ 1 token)"""
        return len(text) // 4