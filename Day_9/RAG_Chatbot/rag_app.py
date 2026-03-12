import chainlit as cl
from openai import AsyncOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

client = AsyncOpenAI()

# Load FAISS index
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

@cl.on_chat_start
async def start():
    cl.user_session.set("chat_history", [])

@cl.on_message
async def main(message: cl.Message):

    chat_history = cl.user_session.get("chat_history")

    # Retrieve relevant documents
    results = vectorstore.similarity_search(message.content, k=2)
    context = "\n\n".join([doc.page_content for doc in results])

    # Build conversation history string
    history_text = ""
    for role, content in chat_history:
        history_text += f"{role}: {content}\n"

    prompt = f"""
You are a helpful assistant.

Use the retrieved context to answer.

Conversation History:
{history_text}

Context:
{context}

User Question:
{message.content}
"""

    # Create assistant message
    msg = cl.Message(content="")
    await msg.send()

    stream = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    full_response = ""

    async for chunk in stream:
        token = chunk.choices[0].delta.content
        if token:
            full_response += token
            await msg.stream_token(token)

    await msg.update()

    # Save conversation
    chat_history.append(("User", message.content))
    chat_history.append(("Assistant", full_response))
    cl.user_session.set("chat_history", chat_history)

























# import chainlit as cl
# from openai import AsyncOpenAI
# from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import FAISS

# client = AsyncOpenAI()

# # Load FAISS index
# embeddings = OpenAIEmbeddings()

# vectorstore = FAISS.load_local(
#     "faiss_index",
#     embeddings,
#     allow_dangerous_deserialization=True
# )

# @cl.on_message
# async def main(message: cl.Message):

#     results = vectorstore.similarity_search(message.content, k=2)

#     context = "\n\n".join([doc.page_content for doc in results])

#     prompt = f"""
# Answer the question using the context below.

# Context:
# {context}

# Question:
# {message.content}
# """

#     msg = cl.Message(content="")
#     await msg.send()

#     stream = await client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         stream=True
#     )

#     async for chunk in stream:
#         token = chunk.choices[0].delta.content
#         if token:
#             await msg.stream_token(token)

#     await msg.update()