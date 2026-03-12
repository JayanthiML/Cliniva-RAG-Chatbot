# CLINIVA – Hospital RAG Chatbot

CLINIVA is an AI-powered **Clinical Assistant Chatbot** built using **LangChain, ChromaDB, OpenAI, and Chainlit**.

It answers hospital-related queries using a **Retrieval-Augmented Generation (RAG)** pipeline built from the official Seven Hills Hospital website content.

---

# Project Overview

CLINIVA works in three major stages:

1. **Data Ingestion & Embedding**
2. **Retrieval-Augmented Generation (RAG) Pipeline**
3. **Interactive Chat UI with Streaming**

When a user asks a question:
 
→ User Query to Retriever (Chroma Vector DB)  
→ Retrieve Relevant Chunks  
→ Inject Context into Prompt  
→ Prompt to OpenAI LLM  
→ Stream Response to UI  

---

# Project Structure

```

RAG_Chatbot_Project/
│
├── app.py                # Chainlit UI (Frontend + Streaming)
├── rag_pipeline.py       # RAG chain logic (Retriever + Augmentation + Generation)
├── vectorstore_db.py     # Web scraping + Embedding + Vector DB creation
├── chroma_db/            # Persistent vector database (generated)
├── .chainlit/config.toml # Chainlit UI configuration
├── .env                  # Environment variables (NOT pushed to Git)
└── README.md

````

---

# File Explanations

---

## `vectorstore_db.py`

This file is responsible for:

- Scraping hospital website data
- Splitting text into chunks
- Generating embeddings
- Storing embeddings in Chroma vector database

### What It Does

- Uses `WebBaseLoader` to scrape:
  - https://www.sevenhillshospital.com/
  - https://www.sevenhillshospital.com/ourdoctorsinmumbai
- Splits text using `RecursiveCharacterTextSplitter`
- Generates embeddings using `OpenAIEmbeddings`
- Stores data in persistent ChromaDB (`chroma_db` folder)

Run this file once before starting the chatbot:

```bash
python vectorstore_db.py
````

This creates the vector database.

---

## `rag_pipeline.py`

This file builds the **RAG pipeline**.

It performs:

* Loads persistent ChromaDB
* Creates retriever (`top k = 3`)
* Defines prompt template
* Initializes OpenAI LLM (`gpt-4o-mini`)
* Builds LangChain RAG chain

### Core Components

* `Chroma` → Vector database
* `Retriever` → Fetch relevant chunks
* `ChatPromptTemplate` → Inject context into LLM
* `ChatOpenAI` → Generate answer
* `StrOutputParser` → Format output

The final object:

```python
rag_chain
```

is used inside `app.py` to generate streaming responses.

---

## `app.py`

This is the **Chainlit frontend application**.

It handles:

* Welcome message
* Quick action buttons
* User message handling
* Streaming responses
* Simple feedback system

### Features

* Branded UI (CLINIVA – Clinical Assistant)
* Quick hospital-related buttons:

  * Schedule Appointment
  * Hospital Location
  * Available Services
* Streaming token-by-token responses
* Simple feedback (Yes / No)
* No data persistence (privacy-friendly)

The chatbot uses:

```python
rag_chain.astream(user_text)
```

to stream responses live.

Run the app:

```bash
chainlit run app.py
```

Open in browser:

```
http://localhost:8000
```

---

# How RAG Works in This Project

1. User asks a question
2. Query is embedded
3. ChromaDB searches for similar chunks
4. Top 3 relevant chunks are retrieved
5. Retrieved content is injected into prompt
6. LLM generates context-aware answer
7. Response is streamed to UI

This prevents hallucination and ensures hospital-specific answers.

---

# Installation Guide

## Clone Repository

```bash
git clone <your_repo_url>
```

## Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Create .env File

```
OPENAI_API_KEY=your_openai_api_key_here
USER_AGENT=Mozilla/5.0
CHAINLIT_AUTH_SECRET=your_chainlit_secret_key
```

---

# Create Vector Database

Run once:

```bash
python vectorstore_db.py
```

This creates the `chroma_db` folder.

---

# Run the Application

```bash
chainlit run app.py
```

---

# Example Questions

* Where is the hospital located?
* What services are available?
* How can I schedule an appointment?
* Who are the doctors available?
* What are the facilities provided?
---

# Tech Stack

* Python
* LangChain
* OpenAI
* ChromaDB
* Chainlit
* Web Scraping
* RAG Architecture

---

# Author

*M L Jayanthi*

---

# Future Improvements

* Add authentication layer
* Add conversational memory
* Show retrieved source snippets
* Add appointment booking form
* Hospital Website access
* Deploy on cloud server
