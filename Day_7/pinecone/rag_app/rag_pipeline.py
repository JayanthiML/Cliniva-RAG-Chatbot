import os
from pinecone import Pinecone
from embedding_model import get_embeddings
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index("rag-index")

client_llm = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

query = input("Ask something: ")

query_embedding = get_embeddings([query])

results = index.query(
    vector=query_embedding[0].tolist(),
    top_k=2,
    include_metadata=True
)

retrieved_docs = [
    match['metadata']['text']
    for match in results['matches']
]

print("\nRetrieved Chunks:\n")

for doc in retrieved_docs:
    print(doc)
    print("-"*40)

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