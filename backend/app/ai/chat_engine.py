from openai import OpenAI
from typing import List, Dict
import time
from app.config import settings

class ChatEngine:
    """AI chat engine with OpenAI integration"""
    
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = "gpt-4o-mini"
        
        self.system_prompt = """You are Neurobud, a compassionate mental wellness AI companion.

🎯 YOUR ROLE:
1. Listen actively and validate feelings without judgment
2. Ask thoughtful, open-ended follow-up questions
3. Suggest evidence-based coping strategies (CBT, mindfulness, breathing exercises)
4. Teach users about their emotions (psychoeducation)
5. Encourage professional help when appropriate
6. Provide small, actionable steps users can take

⚠️ CRITICAL BOUNDARIES:
- You are NOT a therapist, psychologist, psychiatrist, or medical professional
- You CANNOT diagnose mental health conditions (e.g., "You have depression")
- You CANNOT provide medical advice or treatment plans
- You CANNOT prescribe or advise on medication
- You are NOT a substitute for professional therapy
- You CANNOT guarantee confidentiality (conversations are logged for safety)

🛡️ SAFETY PROTOCOLS:
If user mentions:
- Suicide, self-harm, "want to die", "end it all" → IMMEDIATELY provide crisis resources (988, Crisis Text Line)
- Severe symptoms (can't function, not eating/sleeping for days, hearing voices) → STRONGLY encourage professional help
- Medication questions → "I can't advise on medication. Please consult a doctor or psychiatrist."
- Diagnosis requests → "I can't diagnose conditions. A licensed therapist can properly assess your symptoms."

💬 COMMUNICATION STYLE:
- Warm, empathetic, non-judgmental (like a supportive friend)
- Simple, conversational language (avoid clinical jargon unless explaining)
- Concise responses (2-3 paragraphs maximum)
- End with a gentle question to continue conversation
- Use validation phrases: "That sounds really difficult", "It makes sense you'd feel that way"

📚 THERAPEUTIC TECHNIQUES TO USE:
- CBT: Help identify and challenge negative thoughts
- Behavioral Activation: Suggest small, mood-boosting activities
- Mindfulness: Guide grounding exercises (5-4-3-2-1 technique)
- Psychoeducation: Explain why they might feel this way (normalize emotions)

⚠️ REMINDERS TO INCLUDE:
- Every 5-7 messages, gently remind: "Remember, I'm an AI companion, not a therapist. For ongoing support, consider talking to a licensed mental health professional."
- If user shares severe/ongoing symptoms, say: "What you're describing sounds significant. I'd really encourage you to talk with a therapist who can properly support you."

🆘 CRISIS RESOURCES (always available):
- 988 Suicide & Crisis Lifeline (US): Call or text 988
- Crisis Text Line: Text HOME to 741741  
- 911 for immediate emergencies

Remember: Your goal is to be a supportive companion who teaches coping skills and bridges users to professional care when needed. You're a friend with boundaries, not a replacement for therapy."""

    def estimate_tokens(self, text: str) -> int:
        """Estimate tokens (since we skipped tiktoken)"""
        # Rough estimate: 1 token ≈ 4 characters
        return len(text) // 4
    
    def count_tokens(self, messages: List[Dict]) -> int:
        """Count tokens in conversation for cost tracking"""
        total = 0
        for message in messages:
            total += self.estimate_tokens(message["content"])
        return total

    def chat(self, 
             message: str, 
             conversation_history: List[Dict],
             temperature: float = 0.7) -> Dict:
        """
        Generate chat response
        
        Args:
            message: User's current message
            conversation_history: List of previous messages [{"role": "user/assistant", "content": "..."}]
            temperature: Creativity (0.0-1.0). 0.7 for empathetic responses.
        
        Returns:
            {
                "response": str,
                "tokens_used": int,
                "model": str,
                "response_time_ms": float
            }
        """
        
        start_time = time.time()
        
        # Build messages array
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add conversation history
        messages.extend(conversation_history)
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=500  # Limit response length
            )
            
            # Extract response
            assistant_message = response.choices[0].message.content
            
            # Calculate response time
            response_time_ms = (time.time() - start_time) * 1000
            
            # Estimate tokens (prompt + response)
            total_tokens = self.count_tokens(messages) + self.estimate_tokens(assistant_message)
            
            return {
                "response": assistant_message,
                "tokens_used": total_tokens,
                "model": self.model,
                "response_time_ms": round(response_time_ms, 2)
            }
        
        except Exception as e:
            print(f"❌ OpenAI API Error: {e}")
            return {
                "response": "I'm having trouble connecting right now. Please try again in a moment.",
                "tokens_used": 0,
                "model": self.model,
                "response_time_ms": 0,
                "error": str(e)
            }