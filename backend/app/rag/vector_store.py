"""
Vector Store for Mental Health Knowledge Base
Uses Chroma DB for local vector storage with OpenAI embeddings
"""

import chromadb
from chromadb.config import Settings
import os
from typing import List, Dict
from openai import OpenAI
from app.config import settings
from app.rag.knowledge_base import get_all_articles, get_article_count

class VectorStore:
    """Manages vector embeddings and similarity search"""
    
    def __init__(self):
        """Initialize Chroma client and collection"""
        
        # Create persistent storage directory
        persist_directory = os.path.join(os.getcwd(), "chroma_db")
        os.makedirs(persist_directory, exist_ok=True)
        
        # Initialize PERSISTENT Chroma client
        self.client = chromadb.PersistentClient(path=persist_directory)
        
        # Get or create collection
        self.collection_name = "mental_health_kb"
        
        # List existing collections
        existing_collections = [col.name for col in self.client.list_collections()]
        
        if self.collection_name in existing_collections:
            self.collection = self.client.get_collection(self.collection_name)
            count = self.collection.count()
            print(f"[OK] Loaded existing collection: {self.collection_name} ({count} documents)")
        else:
            self.collection = self.client.create_collection(
                name=self.collection_name,
                metadata={"description": "Mental health knowledge base"}
            )
            print(f"[OK] Created new collection: {self.collection_name}")
        
        # Initialize OpenAI client
        self.openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    def get_embedding(self, text: str) -> List[float]:
        """
        Get embedding for text using OpenAI's text-embedding-3-small
        
        Cost: ~$0.02 per 1M tokens (very cheap!)
        """
        try:
            response = self.openai_client.embeddings.create(
                model="text-embedding-3-small",
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"[ERROR] Embedding failed: {e}")
            raise
    
    def add_articles(self, force_recreate: bool = False):
        """
        Add all articles to vector store
        
        Args:
            force_recreate: If True, delete and recreate all embeddings
        """
        
        articles = get_all_articles()
        
        # Check if already populated
        existing_count = self.collection.count()
        if existing_count > 0 and not force_recreate:
            print(f"[INFO] Collection already has {existing_count} documents. Skipping embedding.")
            print("[INFO] Use force_recreate=True to recreate embeddings")
            return
        
        if force_recreate and existing_count > 0:
            print(f"[INFO] Deleting existing {existing_count} documents...")
            self.client.delete_collection(self.collection_name)
            self.collection = self.client.create_collection(
                name=self.collection_name,
                metadata={"description": "Mental health knowledge base"}
            )
        
        print(f"[EMBEDDING] Processing {len(articles)} articles...")
        print("[INFO] This will cost approximately $0.01 in OpenAI credits")
        
        # Prepare data for batch insertion
        documents = []
        metadatas = []
        ids = []
        
        for i, article in enumerate(articles):
            # Combine title and content for richer context
            full_text = f"Title: {article['title']}\n\nCategory: {article['category']}\n\n{article['content']}"
            
            documents.append(full_text)
            metadatas.append({
                "article_id": article["id"],
                "title": article["title"],
                "category": article["category"]
            })
            ids.append(article["id"])
            
            if (i + 1) % 10 == 0:
                print(f"[PROGRESS] Prepared {i + 1}/{len(articles)} articles...")
        
        print("[EMBEDDING] Generating embeddings... (this may take 30-60 seconds)")
        
        embeddings = []
        total_tokens = 0
        
        for i, doc in enumerate(documents):
            embedding = self.get_embedding(doc)
            embeddings.append(embedding)
            
            # Estimate tokens (rough: ~4 chars per token)
            total_tokens += len(doc) // 4
            
            if (i + 1) % 10 == 0:
                print(f"[PROGRESS] Embedded {i + 1}/{len(documents)} articles...")
        
        # Add to collection
        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
        # Calculate cost
        cost = (total_tokens / 1_000_000) * 0.020  # $0.020 per 1M tokens
        
        print(f"[SUCCESS] ✅ Added {len(articles)} articles to vector store!")
        print(f"[COST] Total tokens: {total_tokens:,}")
        print(f"[COST] Estimated cost: ${cost:.4f}")
        print(f"[INFO] Collection now has {self.collection.count()} documents")
    
    def search(self, query: str, n_results: int = 3) -> List[Dict]:
        """
        Search for relevant articles using semantic similarity
        
        Args:
            query: User's question or search query
            n_results: Number of results to return (default 3)
        
        Returns:
            List of relevant articles with metadata
        """
        
        if self.collection.count() == 0:
            print("[WARNING] Vector store is empty. Run add_articles() first.")
            return []
        
        try:
            # Get embedding for query
            query_embedding = self.get_embedding(query)
            
            # Search for similar documents
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=min(n_results, self.collection.count())
            )
            
            # Format results
            formatted_results = []
            if results and results['documents'] and len(results['documents']) > 0:
                for i in range(len(results['documents'][0])):
                    formatted_results.append({
                        "article_id": results['ids'][0][i],
                        "title": results['metadatas'][0][i]['title'],
                        "category": results['metadatas'][0][i]['category'],
                        "content": results['documents'][0][i],
                        "distance": results['distances'][0][i] if 'distances' in results else None
                    })
            
            return formatted_results
        
        except Exception as e:
            print(f"[ERROR] Search failed: {e}")
            import traceback
            traceback.print_exc()
            return []
    
    def get_stats(self) -> Dict:
        """Get statistics about the vector store"""
        return {
            "total_articles": self.collection.count(),
            "collection_name": self.collection_name,
            "kb_article_count": get_article_count()
        }

# Singleton instance
_vector_store = None

def get_vector_store() -> VectorStore:
    """Get or create singleton vector store instance"""
    global _vector_store
    if _vector_store is None:
        _vector_store = VectorStore()
    return _vector_store