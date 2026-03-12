# Day 9 – Building LLM Interfaces with Streamlit & Chainlit

## Overview

The objective of Day 9 was to build **interactive user interfaces for LLM applications** using two popular frameworks:

* **Streamlit** – for building data apps and chat interfaces quickly
* **Chainlit** – for building conversational AI applications

The work involved:

* Creating a **chatbot UI using Streamlit**
* Building a similar interface using **Chainlit**
* Integrating **response streaming**
* Implementing **RAG-based question answering**
* Running the applications locally

---

# Framework Overview

## Streamlit

Streamlit is a Python framework used to create **interactive web applications for data science and AI**.

Advantages:

* Simple Python-based UI creation
* Fast prototyping
* Built-in components for chat interfaces
* Easy local deployment

Documentation:
https://docs.streamlit.io

---

## Chainlit

Chainlit is designed specifically for **LLM-based conversational applications**.

Advantages:

* Built-in chat interface
* Supports LLM streaming
* Conversation history management
* Easy integration with LangChain and OpenAI

Documentation:
https://docs.chainlit.io

---

# Project Structure

```text
Day_9
│
├── Streamlit_App
│   ├── app.py
│
├── Chainlit_App
│   ├── app.py
│   ├── app1.py
│
├── RAG_App
│   ├── rag_app.py
│   ├── create_index.py

```

---

# Streamlit Chatbot Implementation

A **ChatGPT-like interface** was implemented using Streamlit.

Key features:

* Chat interface
* Conversation history
* Streaming responses
* OpenAI integration

Example UI initialization:

```python
st.title("ChatGPT-like clone")
```

The chat history is stored using **Streamlit Session State**.

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

User messages and assistant responses are stored in this state and rendered in the UI. 

---

# Streaming Implementation in Streamlit

Streaming was enabled using the OpenAI API.

```python
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=st.session_state.messages,
    stream=True
)
```

Streamlit’s built-in function was used to display tokens incrementally:

```python
response = st.write_stream(stream)
```

This allows responses to appear **token-by-token in real time**. 

---

# Chainlit Chatbot Implementation

A similar chatbot interface was implemented using **Chainlit**.

Chainlit automatically provides a chat UI with minimal code.

Basic message handler:

```python
@cl.on_message
async def main(message: cl.Message):
```

User messages are received and processed asynchronously.

Responses are streamed back to the UI using:

```python
await msg.stream_token(token)
```

This allows the assistant response to appear gradually in the interface. 

---

# Authentication in Chainlit

A simple login system was implemented.

```python
@cl.password_auth_callback
def auth(username: str, password: str):
```

This ensures only authorized users can access the chatbot interface. 

---

# RAG Integration

A Retrieval-Augmented Generation pipeline was integrated with Chainlit.

Steps:

1. Load vector database
2. Retrieve relevant document chunks
3. Combine context with user query
4. Send prompt to LLM
5. Stream response back to UI

FAISS was used as the vector database.

Vector store loading:

```python
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)
```

Relevant documents are retrieved using similarity search. 

---

# Vector Index Creation

Before running the RAG app, a FAISS index was created from the document.

Steps:

1. Load document
2. Split text into chunks
3. Generate embeddings
4. Store vectors in FAISS index

Example:

```python
vectorstore = FAISS.from_documents(documents, embeddings)
vectorstore.save_local("faiss_index")
```

This allows fast semantic search over document content. 

---

# Response Streaming in Chainlit

Streaming responses were implemented using asynchronous OpenAI calls.

Example:

```python
async for chunk in stream:
    token = chunk.choices[0].delta.content
    await msg.stream_token(token)
```

This ensures the chatbot response appears gradually during generation. 

---

# Running the Applications

## Run Streamlit App

```bash
streamlit run app.py
```

The application runs locally at:

```
http://localhost:8501
```

---

## Run Chainlit App

```bash
chainlit run app.py
```

The interface opens in the browser automatically.

---

# Key Features Implemented

Streamlit App

* ChatGPT-like chatbot interface
* Conversation history
* Streaming responses

Chainlit App

* Chat interface for LLM interaction
* Streaming responses
* Conversation memory
* Authentication support

RAG Application

* FAISS vector database
* Document retrieval
* Context-aware responses

---

# Modules Used

| Module                   | Purpose                     |
| ------------------------ | --------------------------- |
| streamlit                | Build web UI                |
| chainlit                 | Conversational AI interface |
| openai                   | LLM API                     |
| langchain_openai         | Embedding generation        |
| langchain_community      | Vector store                |
| FAISS                    | Vector database             |
| langchain_text_splitters | Document chunking           |

---

# Outcome

This task demonstrated how to build **user-facing interfaces for LLM applications**.

Key achievements:

* Developed chatbot interfaces using Streamlit and Chainlit
* Implemented response streaming
* Integrated a RAG pipeline with FAISS
* Built a fully interactive LLM-powered Q&A application

These interfaces enable users to interact with LLM systems through **real-time conversational interfaces**.