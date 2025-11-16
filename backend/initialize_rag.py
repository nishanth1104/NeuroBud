"""
Initialize RAG system by creating embeddings for knowledge base
Run this once to set up the vector store
"""
# -*- coding: utf-8 -*-

import sys
import io

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from app.rag.vector_store import get_vector_store
from app.rag.knowledge_base import get_article_count

print("=" * 60)
print("NEUROBUD RAG INITIALIZATION")
print("=" * 60)

print(f"\nKnowledge Base: {get_article_count()} articles")
print("Vector Store: Chroma DB (local)")
print("Embeddings: OpenAI text-embedding-3-small")
print("Estimated Cost: ~$0.01\n")

# Get vector store instance
vector_store = get_vector_store()

# Check current state
stats = vector_store.get_stats()
print(f"Current vector store: {stats['total_articles']} documents\n")

if stats['total_articles'] == 0:
    print("[Initializing] vector store for the first time...\n")
    vector_store.add_articles(force_recreate=False)
else:
    print("[OK] Vector store already initialized!")
    print(f"[INFO] Contains {stats['total_articles']} embedded articles")

    recreate = input("\n[?] Recreate embeddings? (y/N): ").lower().strip()
    if recreate == 'y':
        print("\n[Recreating] embeddings...")
        vector_store.add_articles(force_recreate=True)
    else:
        print("[OK] Using existing embeddings")

print("\n" + "=" * 60)
print("RAG SYSTEM READY!")
print("=" * 60)
print("\n[Stats]:")
final_stats = vector_store.get_stats()
print(f"   - Articles embedded: {final_stats['total_articles']}")
print(f"   - Collection: {final_stats['collection_name']}")
print("\n[OK] You can now use RAG in your chat!")