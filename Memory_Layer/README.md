# AI Memory Chatbot using Zep + OpenAI

## Overview

This project demonstrates how to build a **memory-enabled AI chatbot** using Zep and OpenAI.

Large Language Models are naturally **stateless**, meaning they forget previous conversations unless context is manually provided. This project solves that problem by integrating Zep’s memory layer to store, retrieve, and manage conversational history.

The chatbot can:

* Remember previous conversations
* Retrieve relevant context
* Answer temporal questions
* Maintain personalized interactions across conversations

This project was built as part of learning and experimentation with AI memory systems.

---

# Features

* Persistent conversational memory using Zep
* OpenAI-powered response generation
* Automatic conversation storage
* Context retrieval from previous chats
* Temporal memory testing
* User-specific memory handling
* Interactive CLI chatbot interface
* Notebook-based implementation for experimentation

---

# Project Structure

```bash
memory.ipynb      Main implementation file
README.md         Project documentation
```

Since the entire implementation is currently inside a single notebook, all chatbot logic is handled within `memory.ipynb`.

---

# How It Works

### Step 1: User sends input

The chatbot accepts user input from the command line.

```python
user_input = input("You: ")
```

---

### Step 2: Store conversation in Zep

User messages are stored in Zep.

```python
zep_client.thread.add_messages(...)
```

---

### Step 3: Retrieve previous context

The chatbot retrieves relevant past conversations.

```python
zep_client.thread.get_user_context(...)
```

---

### Step 4: Generate response using OpenAI

Retrieved memory + current user query are sent to OpenAI.

```python
openai_client.chat.completions.create(...)
```

---

### Step 5: Store AI response

The assistant response is stored back into Zep memory.

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

---

## Install Dependencies

```bash
pip install zep-cloud openai python-dotenv
```

---

# Environment Variables

Create a `.env` file:

```bash
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

OR use VS Code notebook execution.

---

# Example Conversation

```bash
You: My name is Jayanthi
AI: Nice to meet you, Jayanthi.

You: I live in Hyderabad
AI: Got it.

You: Where do I live?
AI: You live in Hyderabad.
```

---

# Temporal Memory Testing

This project also supports testing temporal memory scenarios such as:

* Place changes
* Habit changes
* Event sequencing
* Previous conversation recall

Example:

```bash
You: I moved from Hyderabad to Bangalore last month
You: Where was I living before Bangalore?
```

---

# Tech Stack

* Python
* Zep
* OpenAI
* Jupyter Notebook
* python-dotenv

---

# Use Cases

* Personal AI assistants
* Healthcare chatbots
* Educational assistants
* Customer support systems
* Long-term conversational agents

---

# Key Learning Outcomes

Through this project, I learned:

* Why LLMs are stateless
* Importance of memory in AI systems
* Thread-based conversation storage
* Context retrieval techniques
* Temporal memory handling
* Integration of external memory systems with LLMs

---

# Future Improvements

* Build FastAPI backend
* Add web UI using Streamlit/Chainlit
* Implement episodic memory
* Add semantic search improvements
* Integrate business event streaming into memory

---