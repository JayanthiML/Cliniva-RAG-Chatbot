# ======================= FAISS RAG =======================

import os
import faiss
import pickle
import numpy as np
from embedding_model import get_embeddings
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client_llm = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load FAISS index
index = faiss.read_index(os.path.join(BASE_DIR, "faiss_index.index"))

# Load chunks
with open(os.path.join(BASE_DIR, "faiss_chunks.pkl"), "rb") as f:
    chunks = pickle.load(f)

query = input("Ask something: ")

query_embedding = get_embeddings([query])
query_embedding = np.array(query_embedding).astype("float32")

D, I = index.search(query_embedding, k=2)

retrieved_docs = [chunks[i] for i in I[0]]

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(retrieved_docs):
    print(f"Chunk {i+1}:")
    print(doc)
    print("-"*50)

context = "\n".join(retrieved_docs)

print("\nRETRIEVED CONTEXT:")
print(context)
print("="*70)

prompt = f"""
Answer using the context below.

Context:
{context}

Question:
{query}
"""

response = client_llm.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user", "content":prompt}
    ]
)

print("\nFinal Answer:\n")

print(response.choices[0].message.content)