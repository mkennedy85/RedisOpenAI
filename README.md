# Redis as a Vector Database with OpenAI

This project demonstrates how to use Redis as a vector database with OpenAI embeddings for semantic search applications.

## Overview

Redis, combined with the RediSearch module, can function as a powerful vector database for storing and querying high-dimensional embeddings. This implementation shows how to:

- Store vector embeddings in Redis
- Perform semantic search using OpenAI's embedding models
- Combine vector search with traditional full-text search (hybrid search)
- Compare different indexing strategies (FLAT vs HNSW)

## What's Included

- **[getting-started-with-redis-and-openai.ipynb](getting-started-with-redis-and-openai.ipynb)** - Interactive Jupyter notebook with complete examples
- **nbutils.py** - Helper utilities for downloading and processing Wikipedia sample data
- **docker-compose.yml** - Redis Stack container configuration (if using local Redis)

## Features Demonstrated

### 1. Vector Database Setup
- Connection to Redis with RediSearch module
- Index creation for vector embeddings
- Loading 282 Wikipedia articles with pre-computed embeddings

### 2. Semantic Search
- Query vectorization using OpenAI's `text-embedding-3-small` model
- K-nearest neighbor (KNN) search on vector embeddings
- Cosine similarity-based ranking

### 3. Hybrid Search
- Combining vector search with full-text filtering
- Multi-field queries (title vectors + content filtering)
- Example: Find articles about "Art" that mention "Leonardo da Vinci"

### 4. Index Type Comparison
- **FLAT Index**: Exact brute-force search, simpler implementation
- **HNSW Index**: Approximate nearest neighbor using hierarchical graphs, optimized for large datasets
- Performance benchmarking between both approaches

## Prerequisites

- Python 3.10+
- Redis with RediSearch module (Redis Stack or Redis Cloud)
- OpenAI API key

## Required Libraries

```bash
pip install redis wget pandas openai
```

## Setup

1. **Set up Redis**: Either use Redis Cloud (as shown in notebook) or run locally with Docker:
   ```bash
   docker-compose up -d
   ```

2. **Configure OpenAI API Key**:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

3. **Run the notebook**: Open and execute `getting-started-with-redis-and-openai.ipynb`

## Example Queries

The notebook includes several example searches:

- "modern art in Europe" - Semantic search on title vectors
- "Famous battles in Scottish history" - Content-based semantic search
- Hybrid queries combining vector similarity with text filters

## Results

The implementation successfully:
- Indexes and searches 282 Wikipedia articles
- Provides semantic search with relevance scoring
- Demonstrates sub-second query performance
- Shows practical RAG (Retrieval-Augmented Generation) patterns

## Use Cases

This approach is ideal for:
- Semantic search applications
- Question-answering systems
- Document similarity matching
- RAG systems for LLM applications
- Content recommendation engines

## Additional Resources

- [Redis Stack Documentation](https://redis.io/docs/stack/)
- [RediSearch Documentation](https://redis.io/docs/stack/search/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
