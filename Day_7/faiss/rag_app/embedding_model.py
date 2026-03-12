# ======================= LOAD EMBEDDING MODEL =======================

# To convert textual data into numerical vector embeddings using a pre-trained Sentence Transformer model.

from sentence_transformers import SentenceTransformer

# Load local embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Function to convert text chunks to embeddings
def get_embeddings(text_chunks):
    
    embeddings = model.encode(text_chunks)
    
    return embeddings