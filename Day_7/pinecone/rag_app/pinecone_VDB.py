import os
from pinecone import Pinecone
from dotenv import load_dotenv
from embedding_model import get_embeddings
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index("rag-index")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(BASE_DIR, "sample_data.txt")

with open(file_path, "r", encoding="utf-8") as f:
    data = f.read()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=20
)

chunks = text_splitter.split_text(data)

embeddings = get_embeddings(chunks)

vectors = []

for i in range(len(chunks)):
    vectors.append({
        "id": f"id{i}",
        "values": embeddings[i].tolist(),
        "metadata": {"text": chunks[i]}
    })

index.upsert(vectors=vectors)

print("Stored in Pinecone!")