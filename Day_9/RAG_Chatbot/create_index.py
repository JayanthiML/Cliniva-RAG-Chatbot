from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# Load file
with open("Hospital_Document.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = splitter.split_text(text)
documents = [Document(page_content=d) for d in docs]

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create FAISS index
vectorstore = FAISS.from_documents(documents, embeddings)

# Save index
vectorstore.save_local("faiss_index")

print("FAISS index created successfully!")