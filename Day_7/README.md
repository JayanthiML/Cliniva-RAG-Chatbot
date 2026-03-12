# Retrieval-Augmented Generation (RAG) Pipeline

---

## Overview

This repository contains the implementation of a **Retrieval-Augmented Generation (RAG)** pipeline.

The objective of this project is to enhance Large Language Model (LLM) responses by retrieving relevant information from external documents using a **Vector Database**, and then generating context-aware answers using an LLM.

Unlike traditional LLM-based systems that rely only on pre-trained knowledge, this pipeline retrieves domain-specific information at runtime, thereby reducing hallucinations and improving response accuracy.

---

## RAG Architecture

The implemented workflow follows this architecture:

```
User Query
    ↓
Convert Query → Embedding
    ↓
Vector Database Search
    ↓
Retrieve Relevant Document Chunks
    ↓
Augment Query with Retrieved Context
    ↓
LLM (OpenAI)
    ↓
Context-Aware Final Answer
```

---

## Technologies Used

* Python
* Sentence Transformers (all-MiniLM-L6-v2)
* OpenAI GPT Model
* ChromaDB (Local Vector DB)
* FAISS (Local Vector DB)
* Pinecone (Cloud Vector DB)
* LangChain Text Splitters
* Python Dotenv
* NumPy
* Pickle

---

## Environment Variables Setup

Create a `.env` file in the root directory and add:

```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

Ensure `.env` is added to `.gitignore` to prevent exposing API keys.

---

## Installation

Install the required dependencies:

```
pip install sentence-transformers
pip install chromadb
pip install faiss-cpu
pip install pinecone-client
pip install langchain-text-splitters
pip install python-dotenv
pip install openai
```

---

## Document Ingestion (Vector Store Creation)

Before querying the system, document embeddings must be created and stored in the Vector Database.

### ChromaDB:

```
python chroma/rag_app/chroma_VDB.py
```

### FAISS:

```
python faiss/rag_app/faiss_VDB.py
```

### Pinecone:

```
python pinecone/rag_app/pinecone_VDB.py
```

This step performs:

* Document Loading
* Text Chunking
* Embedding Generation
* Storage in Vector Database

---

## Querying the RAG Pipeline

After ingestion, run the respective pipeline to query the system.

### ChromaDB:

```
python chroma/rag_app/rag_pipeline.py
```

### FAISS:

```
python faiss/rag_app/faiss_rag_pipeline.py
```

### Pinecone:

```
python pinecone/rag_app/pinecone_rag_pipeline.py
```

Each pipeline will:

* Accept user query
* Retrieve semantically similar document chunks
* Augment query with retrieved context
* Send context + query to OpenAI LLM
* Generate final context-based answer

---

## Observability

For demonstration and debugging purposes, the pipelines also display:

* Retrieved Relevant Chunks
* Augmented Prompt (Query + Context)
* Final Generated Answer

This confirms that the LLM output is grounded in retrieved external data.

---

## Notes

* Vector DB folders (`chroma_db`, FAISS index files) are excluded via `.gitignore`.
* These databases are generated during ingestion and need not be pushed to version control.
* Ensure Pinecone Index is created with:

  * Dimension: **384**
  * Metric: **Cosine**

---

## Outcome

Successfully implemented a working RAG system using:

* Local Vector DBs (ChromaDB & FAISS)
* Cloud Vector DB (Pinecone)
* OpenAI LLM for contextual answer generation

This pipeline demonstrates improved response quality through retrieval-based augmentation.

---