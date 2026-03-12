# 📄 RAG Workflow Explanation (Code Walkthrough)

This document explains the working of the Retrieval-Augmented Generation (RAG) pipeline. It provides a file-by-file breakdown of how the system processes external documents to generate context-aware responses.

---

## 🔹 1. embedding_model.py

### Purpose:

To convert textual data into numerical vector embeddings using a pre-trained Sentence Transformer model.

### Code Explanation:

```python
from sentence_transformers import SentenceTransformer
```

Imports the Sentence Transformers library used for generating embeddings.

```python
model = SentenceTransformer("all-MiniLM-L6-v2")
```

Loads a lightweight pre-trained embedding model capable of converting text into semantic vectors.

```python
def get_embeddings(text_chunks):
```

Defines a function that takes text chunks as input.

```python
embeddings = model.encode(text_chunks)
```

Converts the given list of text chunks into numerical vector representations.

```python
return embeddings
```

Returns the generated embeddings.

---

## 🔹 2. vector_store.py

### Purpose:

To load document data, split it into chunks, generate embeddings, and store them inside a persistent ChromaDB vector database.

### Code Explanation:

```python
import chromadb
import os
from embedding_model import get_embeddings
```

Imports ChromaDB for vector storage and embedding function from embedding_model.py.

```python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
```

Gets the absolute path of the current file directory.

```python
client = chromadb.PersistentClient(
    path=os.path.join(BASE_DIR, "chroma_db")
)
```

Initializes a persistent ChromaDB client which stores vector data locally.

```python
collection = client.get_or_create_collection(
    name="rag_collection"
)
```

Creates or loads an existing collection to store embeddings.

```python
file_path = os.path.join(BASE_DIR, "sample_data.txt")
```

Specifies the path to the document file.

```python
with open(file_path, "r", encoding="utf-8") as f:
    data = f.read()
```

Reads content from the document file.

```python
from langchain_text_splitters import CharacterTextSplitter
```

Imports text splitting utility.

```python
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=20
)
```

Splits large text into smaller overlapping chunks for better embedding quality.

```python
chunks = text_splitter.split_text(data)
```

Generates smaller text chunks.

```python
embeddings = get_embeddings(chunks)
```

Converts each chunk into embeddings.

```python
collection.add(
    documents=chunks,
    embeddings=embeddings.tolist(),
    ids=[f"id{i}" for i in range(len(chunks))]
)
```

Stores text chunks and corresponding embeddings inside the ChromaDB collection.

---

## 🔹 3. rag_pipeline.py

(Reference: )

### Purpose:

To integrate retrieved context with LLM for final response generation.

### Code Explanation:

```python
from dotenv import load_dotenv
load_dotenv()
```

Loads API key from .env file.

```python
client_llm = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

Initializes OpenAI LLM client.

```python
query = input("Ask something: ")
```

Accepts user query.

```python
query_embedding = get_embeddings([query])
```

Converts query into embedding.

```python
results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=2
)
```

Retrieves relevant chunks.

```python
context = "\n".join(results['documents'][0])
```

Combines retrieved chunks into context.

```python
prompt = f"""
Context:
{context}

Question:
{query}
"""
```

Creates prompt using retrieved context.

```python
response = client_llm.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content":prompt}]
)
```

Sends prompt to LLM for context-based response generation.

---

## 🔹 Final Workflow

1. Load Document
2. Split into Chunks
3. Convert Chunks into Embeddings
4. Store in Vector DB
5. Convert User Query to Embedding
6. Retrieve Relevant Context
7. Send Context + Query to LLM
8. Generate Final Answer

---

This pipeline ensures the LLM generates responses based on retrieved external knowledge rather than relying solely on pre-trained data.