"""Test RAG system"""
# -*- coding: utf-8 -*-

import sys
import io

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from app.rag.rag_engine import get_rag_engine

print("Testing RAG System...\n")

rag = get_rag_engine()

# Test queries
queries = [
    "How do I manage anxiety?",
    "What are some breathing exercises?",
    "I'm feeling depressed",
]

for query in queries:
    print(f"\n[Query]: {query}")
    print("-" * 60)

    result = rag.generate_rag_response(query, use_rag=True)

    print(f"[Response]: {result['response'][:200]}...")
    print(f"\n[Sources used]: {len(result['sources'])}")
    for source in result['sources']:
        print(f"   - {source['title']} ({source['category']})")
    print(f"[Tokens]: {result['tokens_used']}")
    print(f"[RAG Used]: {result['rag_used']}")
    print("=" * 60)