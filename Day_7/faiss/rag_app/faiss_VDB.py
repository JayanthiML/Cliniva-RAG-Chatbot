# ======================= FAISS STORE =======================

import os
import faiss
import numpy as np
from embedding_model import get_embeddings
from langchain_text_splitters import CharacterTextSplitter
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(BASE_DIR, "sample_data.txt")

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    data = f.read()

# Chunking
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=20
)

chunks = text_splitter.split_text(data)

print("Chunks Loaded:", chunks)

# Create embeddings
embeddings = get_embeddings(chunks)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings)

# Save index
faiss.write_index(index, os.path.join(BASE_DIR, "faiss_index.index"))

# Save chunks mapping
with open(os.path.join(BASE_DIR, "faiss_chunks.pkl"), "wb") as f:
    pickle.dump(chunks, f)

print("FAISS Index created successfully!")