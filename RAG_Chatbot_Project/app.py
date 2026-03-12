import chainlit as cl
from rag_pipeline import rag_chain

@cl.on_chat_start
async def start():
    await cl.Message(
        content=(
            "🏥 **Welcome to Seven Hills Hospital!**\n\n"
            "I am Cliniva, your Clinical Assistant.\n\n"
            "How can I help you today? 😊"
        ),
        actions=[
            cl.Action(
                name="appointment",
                label="Schedule Appointment",
                payload={"message": "Request to schedule an appointment with expert consultants."}
            ),
            cl.Action(
                name="location",
                label="Hospital Location",
                payload={"message": "Where is the hospital located?"}
            ),
            cl.Action(
                name="services",
                label="Available Services",
                payload={"message": "What medical services are available?"}
            ),
        ],
    ).send()

# ----------------------------
# Handle Button Clicks
# ----------------------------

@cl.action_callback("appointment")
@cl.action_callback("location")
@cl.action_callback("services")
async def handle_action(action: cl.Action):
    user_text = action.payload.get("message")
    if user_text:
        await process_query(user_text)

# ----------------------------
# Handle User Input
# ----------------------------

@cl.on_message
async def main(message: cl.Message):
    await process_query(message.content)

# ----------------------------
# Core RAG Logic
# ----------------------------

async def process_query(user_text: str):

    msg = cl.Message(content="")
    await msg.send()

    full_response = ""

    async for chunk in rag_chain.astream(user_text):
        full_response += chunk
        await msg.stream_token(chunk)

    msg.content = full_response
    await msg.update()

    # Simple feedback (no storage)
    await cl.Message(
        content="Did this answer help you? 😊",
        actions=[
            cl.Action(
                name="feedback_yes",
                label="Yes 👍",
                payload={"feedback": "yes"}
            ),
            cl.Action(
                name="feedback_no",
                label="No 👎",
                payload={"feedback": "no"}
            ),
        ],
    ).send()

# ----------------------------
# Feedback Handlers
# ----------------------------

@cl.action_callback("feedback_yes")
async def feedback_yes(action: cl.Action):
    await cl.Message(content="I'm glad I could help! 💙").send()

@cl.action_callback("feedback_no")
async def feedback_no(action: cl.Action):
    await cl.Message(
        content="I'm sorry about that. Please contact the hospital directly for detailed assistance. 📞"
    ).send()

























































































# import chainlit as cl
# from rag_pipeline import rag_chain

# @cl.password_auth_callback
# def auth(username: str, password: str):
#     if username == "admin" and password == "admin":
#         return cl.User(identifier=username)
#     return None


# @cl.on_chat_start
# async def start():
#     await cl.Message(content="Welcome to Medical Assistant Chatbot").send()


# @cl.on_message
# async def main(message: cl.Message):

#     msg = cl.Message(content="")
#     await msg.send()

#     full_response = ""

#     async for chunk in rag_chain.astream(message.content):
#         full_response += chunk
#         await msg.stream_token(chunk)

#     # IMPORTANT: set final content explicitly
#     msg.content = full_response

#     await msg.update()








# import chainlit as cl
# from rag_pipeline import rag_chain

# @cl.password_auth_callback
# def auth(username: str, password: str):
#     if username == "admin" and password == "admin":
#         return cl.User(identifier=username)
#     return None

# @cl.on_chat_start
# async def start():
#     await cl.Message(content="Welcome to Medical Assistant Chatbot").send()

# @cl.on_message
# async def main(message: cl.Message):

#     msg = cl.Message(content="")
#     await msg.send()

#     async for chunk in rag_chain.astream(message.content):
#         await msg.stream_token(chunk)

#     await msg.update()

# @cl.on_feedback
# async def feedback_handler(feedback):
#     print("Feedback received:", feedback)

# @cl.on_chat_resume
# async def resume(thread):
#     print("Resuming thread:", thread.id)