"""
RAG (Retrieval Augmented Generation) Engine
Combines vector search with GPT to provide knowledge-grounded responses
"""

from typing import List, Dict
from app.rag.vector_store import get_vector_store
from openai import OpenAI
from app.config import settings

class RAGEngine:
    """Retrieval Augmented Generation for mental health queries"""
    
    def __init__(self):
        self.vector_store = get_vector_store()
        self.openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    def retrieve_context(self, query: str, n_results: int = 3) -> List[Dict]:
        """
        Retrieve relevant knowledge base articles for a query
        
        Args:
            query: User's question
            n_results: Number of articles to retrieve
        
        Returns:
            List of relevant articles
        """
        return self.vector_store.search(query, n_results=n_results)
    
    def generate_rag_response(
        self,
        user_query: str,
        conversation_history: List[Dict] = None,
        use_rag: bool = True
    ) -> Dict:
        """
        Generate response using RAG approach
        
        Args:
            user_query: User's question
            conversation_history: Previous conversation context
            use_rag: Whether to use knowledge base (True) or just GPT (False)
        
        Returns:
            Dict with response, sources, and metadata
        """
        
        if conversation_history is None:
            conversation_history = []
        
        # Retrieve relevant context if RAG is enabled
        context_articles = []
        if use_rag:
            context_articles = self.retrieve_context(user_query, n_results=3)
        
        # Build system prompt with or without context
        if context_articles:
            # Build context from retrieved articles
            context_text = "\n\n".join([
                f"**{article['title']}** (Category: {article['category']})\n{article['content']}"
                for article in context_articles
            ])
            
            system_prompt = f"""You are Neurobud, an empathetic mental wellness AI assistant with access to expert mental health knowledge.

KNOWLEDGE BASE CONTEXT:
{context_text}

INSTRUCTIONS:
- Use the knowledge base context above to inform your responses
- If the context is relevant, incorporate that information naturally
- If the context doesn't fully answer the question, supplement with your general knowledge
- Always be empathetic, supportive, and non-judgmental
- Provide specific, actionable advice when appropriate
- If discussing serious issues (suicide, self-harm, abuse), always include crisis resources
- Remind users that you're not a replacement for professional help

Crisis Resources:
- 988 Suicide & Crisis Lifeline (call or text)
- Crisis Text Line: Text HOME to 741741
- Emergency: 911
"""
        else:
            # Standard prompt without RAG
            system_prompt = """You are Neurobud, an empathetic mental wellness AI assistant.

INSTRUCTIONS:
- Be supportive, empathetic, and non-judgmental
- Provide helpful coping strategies and emotional support
- If discussing serious issues (suicide, self-harm, abuse), always include crisis resources
- Remind users that you're not a replacement for professional help

Crisis Resources:
- 988 Suicide & Crisis Lifeline (call or text)
- Crisis Text Line: Text HOME to 741741
- Emergency: 911
"""
        
        # Build messages for OpenAI
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add conversation history
        messages.extend(conversation_history)
        
        # Add current user query
        messages.append({"role": "user", "content": user_query})
        
        try:
            # Generate response
            response = self.openai_client.chat.completions.create(
                model=settings.BASE_MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            ai_response = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            
            # Prepare source attribution
            sources = []
            if context_articles:
                sources = [
                    {
                        "title": article["title"],
                        "category": article["category"],
                        "article_id": article["article_id"]
                    }
                    for article in context_articles
                ]
            
            return {
                "response": ai_response,
                "sources": sources,
                "rag_used": use_rag and len(context_articles) > 0,
                "tokens_used": tokens_used,
                "model": settings.BASE_MODEL,
                "context_articles": len(context_articles)
            }
        
        except Exception as e:
            print(f"[ERROR] RAG generation failed: {e}")
            raise
    
    def get_stats(self) -> Dict:
        """Get RAG engine statistics"""
        return {
            "vector_store": self.vector_store.get_stats(),
            "model": settings.BASE_MODEL
        }

# Singleton instance
_rag_engine = None

def get_rag_engine() -> RAGEngine:
    """Get or create singleton RAG engine instance"""
    global _rag_engine
    if _rag_engine is None:
        _rag_engine = RAGEngine()
    return _rag_engine