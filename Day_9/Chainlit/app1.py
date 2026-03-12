# import chainlit as cl
# from openai import AsyncOpenAI

# client = AsyncOpenAI()

# @cl.on_chat_start
# async def start():
#     cl.user_session.set("history", [])

# @cl.on_message
# async def main(message: cl.Message):

#     history = cl.user_session.get("history")

#     # Add user message to history
#     history.append({"role": "user", "content": message.content})

#     response = await client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=history
#     )

#     assistant_reply = response.choices[0].message.content

#     # Add assistant reply to history
#     history.append({"role": "assistant", "content": assistant_reply})

#     cl.user_session.set("history", history)

#     await cl.Message(content=assistant_reply).send()




# ====================================================================================

# ## 2) Without Conversation Memory

# import chainlit as cl
# from openai import AsyncOpenAI

# client = AsyncOpenAI()

# @cl.on_message
# async def main(message: cl.Message):

#     response = await client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "user", "content": message.content}])

#     await cl.Message(content=response.choices[0].message.content).send()

# =======================================================================================

# ## 1) Basic

# import chainlit as cl

# @cl.on_message
# async def main(message: cl.Message):
#     await cl.Message(
#         content=message.content).send()