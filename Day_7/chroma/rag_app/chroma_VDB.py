# ======================= STORE EMBEDDINGS =======================

# To load document data, split it into chunks, generate embeddings, 
# and store them inside a persistent ChromaDB vector database.

import chromadb
import os
from embedding_model import get_embeddings
from langchain_text_splitters import CharacterTextSplitter # Text Splitting Utility


# Absolute path of CWD
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Persistent DB - Initializes a persistent ChromaDB client
client = chromadb.PersistentClient(
    path=os.path.join(BASE_DIR, "chroma_db")
)

# Creates or loads collection
collection = client.get_or_create_collection(
    name="rag_collection"
)

# ------------------ LOAD CHUNKS ------------------

# path of the reference document
file_path = os.path.join(BASE_DIR, "sample_data.txt")

# Reads the contents
with open(file_path, "r", encoding="utf-8") as f:
    data = f.read()

# Splits large text into smaller overlapping chunks for better embedding quality.
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=20
)
chunks = text_splitter.split_text(data)

print("Chunks Loaded:", chunks)

# ------------------ CREATE EMBEDDINGS ------------------
embeddings = get_embeddings(chunks)

# ------------------ STORE IN CHROMA ------------------
collection.add(
    documents=chunks,
    embeddings=embeddings.tolist(),
    ids=[f"id{i}" for i in range(len(chunks))]
)

print("Embeddings stored successfully!")