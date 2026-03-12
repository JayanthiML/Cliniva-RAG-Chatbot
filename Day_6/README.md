# LLM Fundamentals & Prompt Engineering

## Overview

The objective of Day 6 was to understand **Large Language Models (LLMs)** and experiment with **prompt engineering techniques**.

The work included:

* Learning core LLM concepts
* Exploring different LLM providers
* Setting up a working LLM environment using **Google Gemini API**
* Writing Python scripts to test prompts
* Comparing responses across multiple prompting techniques

---

# Understanding Large Language Models

## What is an LLM?

A **Large Language Model (LLM)** is a deep learning model trained on massive amounts of text data.

LLMs generate responses using **next-token prediction**.

Process:

1. Input text is converted into **tokens**
2. The model predicts the **most probable next token**
3. The process repeats until a full response is generated

---

# Key Concepts Learned

## Tokens

Text is broken into smaller units called **tokens**.

Examples:

* word
* part of a word
* punctuation

LLMs process **tokens instead of characters or full sentences**.

---

## Context Window

The **context window** determines how many tokens the model can process at once.

It includes:

* Input tokens
* Output tokens

If the prompt exceeds the context window, the model cannot process the entire text.

---

## Temperature

Temperature controls **randomness in model output**.

Low Temperature

* More deterministic
* More focused responses

High Temperature

* More creative
* More diverse responses

---

## Prompt

A **prompt** is the instruction given to an LLM.

Prompt quality directly affects:

* response accuracy
* reasoning depth
* output format
* tone

---

# LLM Ecosystem Exploration

Different LLM providers were studied.

### OpenAI (GPT Models)

Used via:

* ChatGPT
* OpenAI API

Common use cases:

* chatbots
* automation
* coding assistants

---

### Google Gemini

Used through:

* Google AI Studio
* Gemini API

Advantages:

* easy integration
* strong multimodal support

---

### Meta Llama

Used mostly for **local LLM setups**.

Often run using:

* Ollama
* Local GPU environments

---

# Environment Setup

The Gemini API was configured for programmatic access.

A `.env` file was used to securely store the API key.

Example:

```
GEMINI_API_KEY=your_api_key_here
```

The API key is loaded in Python using **dotenv**.

---

# Testing Gemini API

File used:

```
gemini_llm_test.py
```

Purpose:

* Load environment variables
* Create Gemini client
* Test API connectivity
* List available models

---

# Prompt Experimentation

The goal was to test **how prompt structure changes model responses**.

Base Question Used:

```
Why is the sky blue?
```

Five prompting techniques were tested.

---

# Prompt Testing Script

File used:

```
prompt_testing.py
```

Purpose:

* Send different prompts to the LLM
* Collect responses
* Save outputs for analysis

---

# Prompt Techniques Tested

## 1 Standard Prompt

Prompt:

```
Why is the sky blue?
```

Observation:

* Model produced a detailed explanation
* Structured response
* Clear scientific reasoning

Learning:

Standard prompts work well for general questions but provide limited control over output style.

---

# 2 Persona Prompt

Prompt example:

```
You are a Victorian-era poet. Explain to a curious child why the sky is blue using poetic language.
```

Observation:

* Response style changed dramatically
* Language became poetic and metaphorical
* Scientific depth slightly reduced

Learning:

Persona prompts help control **tone and narrative style**.

---

# 3 Chain-of-Thought Prompting

Prompt structure:

```
1. Define Rayleigh scattering
2. Explain atmospheric interaction
3. Explain why the sky appears blue
```

Observation:

* Output became more structured
* Reasoning steps clearly separated
* Explanation depth increased

Learning:

Chain-of-thought prompting improves **logical reasoning and clarity**.

---

# 4 Constraint-Based Prompting

Prompt example:

```
Explain why the sky is blue.
Use exactly two sentences.
Do not use the words "sun" or "color".
```

Observation:

* Model followed strict instructions
* Response became concise
* Creativity reduced

Learning:

Constraints are useful when controlling:

* response length
* formatting
* UI-limited outputs

---

# 5 Few-Shot Prompting

Prompt example:

```
Q: Why is grass green?
A: Chlorophyll absorbs red/blue light and reflects green.

Q: Why is the ocean blue?
A: Water molecules absorb long-wave reds and scatter blues.

Q: Why is the sky blue?
A:
```

Observation:

* Model followed the example pattern
* Output became short and structured

Learning:

Few-shot prompting improves **format consistency and predictability**.

Example results were stored in JSON format for comparison. 

---

# Output Documentation

Two files were generated for documentation:

### prompts.txt

Contains readable logs of each prompt and response. 

### prompt_experimentation.json

Contains structured results for analysis.

---

# Key Insights

Major findings from prompt experimentation:

* Prompt structure significantly affects response quality.
* Clear instructions improve reasoning depth.
* Few-shot examples improve output consistency.
* Constraint prompts control verbosity and format.
* Persona prompts influence tone and narrative style.

---

# Conclusion

This exercise demonstrated:

* Core concepts of Large Language Models
* Prompt engineering techniques
* API integration with Gemini
* Automated prompt testing using Python
* Response analysis across different prompting styles

Understanding prompt engineering is essential when designing systems powered by LLMs such as:

* AI assistants
* chatbots
* automated documentation tools
* code generation systems