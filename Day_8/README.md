# Response Streaming & Advanced Prompting

## Overview

The objective of this task was to explore **LLM response streaming** and **advanced prompting techniques**.

The work focused on:

* Implementing **streaming and non-streaming responses**
* Comparing **latency and user experience**
* Testing streaming with both **Local LLM (Ollama)** and **OpenAI API**
* Experimenting with advanced prompting strategies:

  * Normal Prompting
  * Few-Shot Prompting
  * Chain-of-Thought (CoT)
  * Few-Shot + CoT

The experiments also measured **generation time and time-to-first-token**.

---

# Response Streaming

## What is Streaming?

In standard LLM responses, the model generates the entire output first and then returns the complete result.

Streaming changes this behavior by sending **tokens incrementally** as they are generated.

This allows applications to display responses **in real time**.

---

# Streaming vs Non-Streaming

### Non-Streaming

* The model processes the entire response.
* The full response is returned only after completion.
* The user waits without any intermediate output.

Example implementation:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"Explain Artificial Intelligence"}]
)
```

The result appears only after the model finishes generating the response. 

---

### Streaming

Streaming sends tokens as soon as they are generated.

Example:

```python
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"Explain Artificial Intelligence"}],
    stream=True
)
```

Each token is printed as soon as it arrives. 

---

# Implementations

Two environments were used to test streaming behavior.

### 1. Local LLM – Ollama

Model used:

```
phi
```

Library used:

```
ollama
```

---

## Ollama Non-Streaming

The response is generated completely before being returned.

Example:

```python
response = ollama.chat(
    model='phi',
    messages=[{'role':'user','content':'Write exactly 200 words explaining Artificial Intelligence'}]
)
```

Execution time is measured after the full response is generated. 

---

## Ollama Streaming

Streaming was enabled using:

```
stream=True
```

Tokens were printed incrementally while measuring **time-to-first-token**.

Example:

```python
for chunk in stream:
    print(chunk['message']['content'], end='')
```

This allows the user to see the response while it is being generated. 

---

# OpenAI API Implementation

Model used:

```
gpt-4o-mini
```

Library used:

```
openai
```

---

## OpenAI Non-Streaming

The full response is returned after completion.

Example:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"Explain Artificial Intelligence"}]
)
```

Execution time was measured after receiving the complete output. 

---

## OpenAI Streaming

Streaming was enabled using:

```
stream=True
```

Tokens were printed immediately when received.

Example:

```python
for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
```

This displays the response gradually during generation. 

---

# Latency Comparison

The following results were measured during experimentation.

## Ollama (Local LLM)

Non-Streaming Total Time

```
52.26 seconds
```

Streaming Time to First Token

```
0.4 seconds
```

Streaming Total Time

```
47.15 seconds
```

---

## OpenAI API

Non-Streaming Total Time

```
7.92 seconds
```

Streaming Time to First Token

```
2.77 seconds
```

Streaming Total Time

```
8.1 seconds
```

Results recorded during testing. 

---

# Streaming vs Non-Streaming User Experience

Non-streaming returns the full response only after generation is completed, causing the user to wait without any feedback.

Streaming sends tokens incrementally, allowing the user to see the response as it is being generated.

Although the total generation time is nearly the same, **streaming significantly improves perceived responsiveness and user experience**.

---

# Advanced Prompting Techniques

Advanced prompting methods were tested to observe differences in reasoning and response structure.

The following math problem was used:

```
The cafeteria had 23 apples. 
They used 20 apples to make lunch and then bought 6 more.
How many apples do they have now?
```

Model used:

```
gpt-4o-mini
```

Temperature:

```
0
```

Using temperature 0 ensured **deterministic responses**.

Implementation reference: `CoT_FSP.py` 

---

# Prompting Techniques Tested

## 1. Normal Prompting

Direct question without additional guidance.

Observation:

* Correct answer produced
* Minimal reasoning
* Simple explanation

Example output shows basic calculation steps. 

---

## 2. Few-Shot Prompting

Provided an example question and answer before the actual question.

Observation:

* Output structure followed the example pattern
* More consistent formatting
* Clearer step breakdown

Learning:

Few-shot prompting helps enforce **consistent response structure**.

---

## 3. Chain-of-Thought Prompting

Explicit instruction to **show reasoning step-by-step**.

Observation:

* Detailed reasoning
* Transparent intermediate calculations
* Clear logical flow

Learning:

Chain-of-Thought improves **interpretability and reasoning clarity**.

---

## 4. Few-Shot + Chain-of-Thought

Combined example-based learning with step-by-step reasoning.

Observation:

* Most structured explanation
* Clear logical reasoning
* Consistent formatting

Learning:

Combining **few-shot examples with chain-of-thought prompting** provides the most reliable structured responses.

---

# Modules Used

| Module | Purpose                      |
| ------ | ---------------------------- |
| openai | LLM API integration          |
| ollama | Local LLM interaction        |
| time   | Latency measurement          |
| dotenv | Environment variable loading |

---

# Outcome

The experiments successfully demonstrated:

* Implementation of **real-time LLM response streaming**
* Comparison between streaming and non-streaming responses
* Latency measurement using **time-to-first-token**
* Practical use of **advanced prompting techniques**

Streaming was found to significantly improve **perceived response speed and user experience**, while advanced prompting techniques improved **reasoning clarity and output structure**.