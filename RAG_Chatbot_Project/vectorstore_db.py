import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

# Load website
loader = WebBaseLoader(web_paths=['https://www.sevenhillshospital.com/',
                                  'https://www.sevenhillshospital.com/ourdoctorsinmumbai'])

docs = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
splits = text_splitter.split_documents(docs)

# ----------------------------------------------------------------------------

## Vectorization

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "sevenhills-index"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(index_name)

# Create Vector Store

vectorstore = PineconeVectorStore.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings(),
    index_name=index_name)

print("Pinecone vector store created successfully!")