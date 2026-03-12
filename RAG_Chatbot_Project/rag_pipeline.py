import os
from dotenv import load_dotenv
load_dotenv()
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load DB

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("sevenhills-index")

vectorstore = PineconeVectorStore(
    index=index,
    embedding=OpenAIEmbeddings()
)

# Retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Augmentation
prompt = ChatPromptTemplate.from_template("""
You are a Medical Assistant Chatbot.
Use the retrieved context to answer the question.
If you don't get any context. Tell to contact the Hospital Directly.
                                          
Context:
{context}

Question:
{question}

Answer:
""")

# Model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    streaming=True
)

# to format the retrieved chunks
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Rag Pipeline using runnables
rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()                             # formats the output from the LLM
)