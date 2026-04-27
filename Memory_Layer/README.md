# AI Memory Architecture with Zep + OpenAI

## Overview

Large Language Models (LLMs) are inherently **stateless**, meaning they do not retain memory between conversations unless relevant context is explicitly provided.

This project explores how to build a **memory-enabled AI system** using **Zep Cloud** and **OpenAI**, where user conversations are stored, transformed into structured memory, and later retrieved to generate context-aware responses.

The project focuses on understanding how modern AI memory systems work in real-world applications such as:

- Healthcare assistants  
- Personal AI assistants  
- Customer support bots  
- Enterprise copilots  
- Long-term conversational systems  

---

## Problem Statement

Traditional LLM applications suffer from:

- No long-term memory  
- Context window limitations  
- Poor personalization  
- Difficulty handling evolving user information  
- Manual prompt engineering for context retrieval  

This project addresses these challenges by integrating **Zep’s memory layer**.

---

# How Zep Works in This Project

```text
User Conversation
       ↓
Thread Storage
       ↓
Automatic Memory Extraction
       ↓
Graph-Based Memory Storage
       ↓
Relevant Memory Retrieval
       ↓
Context Construction
       ↓
OpenAI Response Generation
```

---

## Core Concepts Implemented

### 1. Thread-Based Conversation Storage

Stores raw conversations in Zep threads.

```python
zep_client.thread.add_messages(...)
```

This preserves complete conversation history.

---

## 2. Automatic Graph Memory Creation

Zep automatically extracts:

- Entities  
- Facts  
- Relationships  
- Temporal information  

Example:

```text
User → WAS_DIAGNOSED_WITH → Diabetes
User → TAKES → Metformin
User → LIVES_IN → Hyderabad
```

---

## 3. Memory Retrieval

Retrieve relevant memories from the graph.

```python
zep_client.graph.search(...)
```

Example retrieval:

- Medical history  
- Personal preferences  
- User profile  
- Appointment details  

---

## 4. Automatic Context Retrieval

Zep can automatically generate LLM-ready context.

```python
zep_client.thread.get_user_context(...)
```

---

## 5. Custom Context Construction

This project also explores manually creating context using retrieved graph memories.

```python
custom_context = f"""
PATIENT HEALTH CONTEXT:
{retrieved_memories}
"""
```

This gives full control over what gets sent to the LLM.

---

## Features

- Persistent memory storage  
- Graph-based memory extraction  
- Temporal memory handling  
- Custom context construction  
- Automatic context retrieval  
- Personalized conversation support  
- OpenAI integration  
- Jupyter notebook experimentation  

---

## Example Conversation Used for Testing

The system was tested with mixed user information such as:

- Name  
- Age  
- Location  
- Profession  
- Family details  
- Medical history  
- Medications  
- Allergies  
- Appointments  
- Food preferences  
- Travel preferences  
- Lifestyle habits  

Example:

```text
My name is John Miller
I live in Hyderabad
I was diagnosed with diabetes
I take Metformin daily
I prefer morning appointments
```

---

## Tech Stack

- Python  
- Zep Cloud  
- OpenAI API  
- Jupyter Notebook  
- python-dotenv  

---

# Project Structure

```bash
memory.ipynb
README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

## Install Dependencies

```bash
pip install zep-cloud openai python-dotenv
```

---

## Environment Variables

Create a `.env` file:

```env
ZEP_API_KEY=your_zep_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

# Running the Project

Open Jupyter Notebook:

```bash
jupyter notebook
```

Run:

```bash
memory.ipynb
```

---

# Key Learnings

Through this project, I learned:

- Why LLMs are stateless  
- Difference between memory vs context  
- Thread-based storage architecture  
- Graph-based memory extraction  
- Temporal memory systems  
- Automatic vs custom context generation  
- Limitations of conversation-only memory systems  
- When structured databases may be better than conversational memory extraction  

---

# Future Improvements

- FastAPI integration  
- Streamlit UI  
- Chainlit chatbot interface  
- Database integration  
- Hybrid memory systems  
- Better memory filtering mechanisms  

---

# Real-World Use Cases

- Healthcare assistants  
- Customer support systems  
- Personal assistants  
- Enterprise copilots  
- Financial assistants  
- E-commerce assistants  

---

## Key Insight

**Memory ≠ Context**

Zep stores memory:

- Conversations  
- Facts  
- Relationships  

Your application decides how to retrieve and assemble the right context before sending it to the LLM.

This project helped understand how production-grade AI memory systems are built.