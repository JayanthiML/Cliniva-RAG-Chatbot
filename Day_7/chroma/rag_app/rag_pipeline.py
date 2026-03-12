# ======================= RAG PIPELINE =======================

# To integrate retrieved context with LLM for final response generation.

import chromadb
import os
from embedding_model import get_embeddings
from openai import OpenAI
from dotenv import load_dotenv

# Loads API Key 
load_dotenv()

# Initializes OpenAI LLm Client
client_llm = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Vector DB
client = chromadb.PersistentClient(
    path=os.path.join(BASE_DIR, "chroma_db")
)

# Collection
collection = client.get_or_create_collection(
    name="rag_collection"
)

# ------------------ USER QUERY ------------------

query = input("Ask something: ")

# Convert query to embedding
query_embedding = get_embeddings([query])

# Retrieve relevant chunks
# Searches for top 2 most similar document chunks.
results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=2
)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(results['documents'][0]):
    print(f"Chunk {i+1}:")
    print(doc)
    print("-" * 50)

# Combines retrieved chunks into context
context = "\n".join(results['documents'][0])

print("\nRETRIEVED CONTEXT:")
print(context)
print("=" * 70)
# ------------------ PROMPT ------------------

prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}
"""

# ------------------ LLM RESPONSE ------------------

# Sends prompt to LLM for context-based response generation.

response = client_llm.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user", "content":prompt}
    ]
)

print("\nFinal Answer:\n")

print(response.choices[0].message.content)