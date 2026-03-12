# LLM Engineering Practice Projects

## Overview

This repository contains a collection of **hands-on projects completed during an LLM Engineering internship practice series**.
The work progresses from **building APIs → understanding LLMs → implementing RAG systems → creating AI-powered applications**.

The projects demonstrate practical implementations of:

* FastAPI REST APIs
* Prompt Engineering
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* LLM Response Streaming
* AI-powered Chatbot Interfaces

---

# Project Structure

```text
Practice_works
│
├── Day_3    → Database Integration with Python
├── Day_4_5  → FastAPI CRUD API
├── Day_6    → LLM Fundamentals & Prompt Engineering
├── Day_7    → Retrieval-Augmented Generation (RAG)
├── Day_8    → Response Streaming & Advanced Prompting
├── Day_9    → Streamlit & Chainlit Chatbot Applications
│
└── README.md
```

---

# Day-wise Summary

### Day 4 – FastAPI Basics

* Built REST APIs using **FastAPI**
* Implemented **GET and POST endpoints**
* Used **Pydantic for request validation**
* Tested APIs using **Swagger and Postman**

---

### Day 5 – CRUD API Project

Created a **Student Management CRUD API**.

Endpoints implemented:

* GET students
* POST student
* PUT update student
* DELETE student

Database integrations explored:

* **MySQL**
* **MongoDB**

---

### Day 6 – LLM Fundamentals & Prompt Engineering

Learned core LLM concepts:

* Tokens
* Context Window
* Temperature
* Prompt Structure

Prompting techniques tested:

* Standard Prompting
* Persona Prompting
* Chain-of-Thought
* Constraint Prompting
* Few-Shot Prompting

---

### Day 7 – Retrieval-Augmented Generation (RAG)

Built a complete **RAG pipeline**.

Workflow:

```
User Query
   ↓
Embedding
   ↓
Vector DB Search
   ↓
Retrieve Relevant Chunks
   ↓
Context + Query → LLM
   ↓
Generated Answer
```

Vector databases used:

* **ChromaDB**
* **FAISS**
* **Pinecone**

Embedding model used:

```
all-MiniLM-L6-v2
```

---

### Day 8 – Response Streaming & Advanced Prompting

Implemented **real-time streaming responses**.

Tested environments:

* **Ollama (Local LLM – phi model)**
* **OpenAI API – gpt-4o-mini**

Streaming returns tokens incrementally, improving **perceived response speed and user experience**.

Advanced prompting strategies tested:

* Normal prompting
* Few-shot prompting
* Chain-of-thought prompting
* Few-shot + chain-of-thought

---

### Day 9 – Building LLM Interfaces

Built chatbot interfaces using:

**Streamlit**

* ChatGPT-like UI
* Conversation history
* Streaming responses

Run with:

```
streamlit run app.py
```

**Chainlit**

* Conversational AI interface
* Async streaming responses
* Authentication support

Run with:

```
chainlit run app.py
```

Also implemented a **RAG-based Q&A chatbot using FAISS vector database**.

---

# Technologies Used

Backend & APIs

* FastAPI
* Uvicorn
* Pydantic

LLM APIs

* OpenAI
* Gemini
* Ollama

Vector Databases

* ChromaDB
* FAISS
* Pinecone

LLM Tools

* Sentence Transformers
* LangChain

UI Frameworks

* Streamlit
* Chainlit

Utilities

* Python-dotenv
* NumPy
* Pandas

---

# Environment Variables

API keys are stored in `.env` files.

Example:

```
OPENAI_API_KEY=your_key
PINECONE_API_KEY=your_key
GEMINI_API_KEY=your_key
```

`.env` files are excluded from Git using `.gitignore`.

---

# Running the Projects

Install dependencies:

```
pip install -r requirements.txt
```

Run projects from the corresponding day folders.

---

# Outcome

These projects demonstrate practical skills in:

* API development
* LLM integration
* Prompt engineering
* RAG architecture
* Vector databases
* Streaming LLM responses
* Building AI-powered applications