# AI Memory Chatbot using Zep and OpenAI

## Overview

This project implements a context-aware AI chatbot by integrating Zep Cloud for persistent memory and OpenAI for natural language generation. The system overcomes the stateless nature of large language models by storing and retrieving conversation history, enabling more coherent and personalized interactions.

This project is developed as a practice implementation to understand and experiment with memory layers in AI systems.

---

## Features

* Persistent conversational memory using Zep Cloud
* Context-aware responses based on past interactions
* Thread-based conversation management
* Automatic storage of user and assistant messages
* Command-line interface for interaction
* Simple and modular implementation

---

## Architecture

The system follows a memory-augmented pipeline:

1. User input is captured
2. Message is stored in Zep memory
3. Relevant context is retrieved from Zep
4. Context and input are sent to OpenAI
5. Response is generated
6. Assistant response is stored back in Zep

---

## Project Structure

```
memory.py        Main chatbot implementation  
memory.ipynb     Notebook version for testing and experimentation  
README.md        Project documentation  
```

---

## Installation

### Prerequisites

* Python 3.8 or higher
* Zep Cloud API key
* OpenAI API key

### Steps

```bash
git clone <repository-url>
cd <repository-name>
pip install zep-cloud openai python-dotenv
```

---

## Environment Configuration

Create a `.env` file in the root directory:

```
ZEP_API_KEY=your_zep_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

## Usage

Run the chatbot:

```bash
python memory.py
```

You can then interact via the command line. Type `exit` to stop the application.

---

## How It Works

### 1. Client Initialization

The system initializes both Zep and OpenAI clients using API keys loaded from environment variables.

### 2. User and Thread Management

* A unique `user_id` identifies the user
* A `thread_id` represents a conversation session

### 3. Message Storage

Each user input is stored in Zep memory:

```python
zep_client.thread.add_messages(thread_id, messages=[user_msg])
```

### 4. Context Retrieval

Relevant past interactions are retrieved:

```python
user_context = zep_client.thread.get_user_context(thread_id=thread_id)
```

### 5. Response Generation

The retrieved context is passed along with user input to OpenAI:

```python
openai_client.chat.completions.create(...)
```

### 6. Memory Update

The assistant’s response is stored in Zep for future use.

---

## Example Interaction

```
You: My name is Jayanthi
AI: Nice to meet you, Jayanthi.

You: What is my name?
AI: Your name is Jayanthi.
```

---

## Core Implementation

The main logic is implemented in the file: memory.py

---

## Key Concepts

| Concept           | Description                                     |
| ----------------- | ----------------------------------------------- |
| Stateless LLM     | Language models do not retain memory by default |
| Persistent Memory | Zep stores conversation history                 |
| Thread            | Represents a session of interaction             |
| Context Retrieval | Fetches relevant past messages                  |

---

## Use Cases

* AI assistants
* Customer support chatbots
* Healthcare assistants
* Personalized recommendation systems
* Educational tools

---

## Tech Stack

* Python
* Zep Cloud
* OpenAI API
* python-dotenv

---