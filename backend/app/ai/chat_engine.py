import openai
import time
import random
from typing import List, Dict
from app.config import settings
from app.rag.rag_engine import get_rag_engine

class ChatEngine:
    """OpenAI chat engine with A/B testing support and RAG"""
    
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
        self.base_model = settings.BASE_MODEL
        self.fine_tuned_model = settings.FINE_TUNED_MODEL_ID
        self.ab_testing_enabled = settings.AB_TESTING_ENABLED
        self.ab_test_split = settings.AB_TEST_SPLIT
        self.system_prompt = """You are Neurobud, an empathetic AI mental wellness companion specifically designed for mental health support.

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
        user_id: int = None,
        use_rag: bool = True  # NEW: Enable RAG by default
    ) -> Dict:
        """
        Send message to OpenAI and get response with optional RAG enhancement
        
        Args:
            message: User's message
            conversation_history: Previous messages in conversation
            user_id: User ID for consistent A/B assignment
            use_rag: Whether to use RAG (Retrieval Augmented Generation)
            
        Returns:
            Dict with response, tokens_used, model, variant, response_time_ms, rag_used, rag_sources
        """
        
        start_time = time.time()
        
        # Select model (A/B testing)
        model_id, model_variant = self.select_model(user_id)
        
        print(f"[CHAT] Model: {model_id} (variant: {model_variant}), RAG: {use_rag}")
        
        # Use RAG if enabled
        if use_rag:
            try:
                rag_engine = get_rag_engine()
                
                # Prepare conversation history for RAG
                formatted_history = conversation_history if conversation_history else []
                
                # Generate RAG-enhanced response
                rag_result = rag_engine.generate_rag_response(
                    user_query=message,
                    conversation_history=formatted_history[-10:],  # Last 10 messages
                    use_rag=True
                )
                
                response_time = (time.time() - start_time) * 1000
                
                return {
                    "response": rag_result["response"],
                    "tokens_used": rag_result["tokens_used"],
                    "model": model_id,
                    "model_variant": model_variant,
                    "response_time_ms": response_time,
                    "rag_used": True,
                    "rag_sources": rag_result.get("sources", []),
                    "rag_context_articles": rag_result.get("context_articles", 0)
                }
            except Exception as e:
                print(f"[WARNING] RAG failed, falling back to standard chat: {e}")
                # Fall through to standard chat if RAG fails
        
        # Standard chat without RAG (or fallback)
        messages = [
            {
                "role": "system",
                "content": self.system_prompt
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
                "model_variant": model_variant,
                "response_time_ms": response_time_ms,
                "rag_used": False,
                "rag_sources": [],
                "rag_context_articles": 0
            }
            
        except Exception as e:
            print(f"[ERROR] OpenAI API error: {e}")
            raise
    
    def estimate_tokens(self, text: str) -> int:
        """Rough estimation of tokens (4 chars ≈ 1 token)"""
        return len(text) // 4