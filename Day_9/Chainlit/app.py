import chainlit as cl
from openai import AsyncOpenAI

@cl.password_auth_callback
def auth(username: str, password: str):
    # Replace these with whatever credentials you want
    if username == "admin" and password == "admin123":
        return cl.User(identifier=username)
    return None

client = AsyncOpenAI()

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])

@cl.on_message
async def main(message: cl.Message):

    history = cl.user_session.get("history")

    history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")
    await msg.send()

    stream = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history,
        stream=True
    )

    full_response = ""

    async for chunk in stream:
        delta = chunk.choices[0].delta
        if delta and delta.content:
            token = delta.content
            full_response += token
            await msg.stream_token(token)
    await msg.update()
    history.append({"role": "assistant", "content": full_response})
    cl.user_session.set("history", history)

@cl.on_feedback
async def feedback_handler(feedback):
    print("Feedback received:", feedback)