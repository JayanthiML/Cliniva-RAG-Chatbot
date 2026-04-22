import os
import uuid
import json
from dotenv import load_dotenv
from datetime import datetime, timezone

from zep_cloud.client import Zep
from zep_cloud.types import Message
from openai import OpenAI

load_dotenv()

ZEP_API_KEY = os.getenv("ZEP_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Clients

zep_client = Zep(api_key=ZEP_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

print("✅ Clients initialized")

# Create User

user_id = "jayanthi_001"

# zep_client.user.add(
#     user_id=user_id
# )

# print("✅ User created")

# Create Thread

thread_id = uuid.uuid4().hex

zep_client.thread.create(
    thread_id=thread_id,
    user_id=user_id,
)

print("✅ Thread created:", thread_id)

# Function for chat Agent

def chat_with_agent(user_input):

    # ---- Store user message in Zep ----
    user_msg = Message(
        created_at=datetime.now(timezone.utc).isoformat(),
        name="Jayanthi",
        role="user",
        content=user_input,
    )

    zep_client.thread.add_messages(thread_id, messages=[user_msg])

    # ---- Get context from Zep ----
    user_context = zep_client.thread.get_user_context(thread_id=thread_id)
    context_block = user_context.context

    # ---- Send to OpenAI ----
    response = openai_client.chat.completions.create(
        model="gpt-4.1-mini",   
        messages=[
            {
                "role": "system",
                "content": context_block
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    answer = response.choices[0].message.content

    # ---- Store assistant response in Zep ----
    assistant_msg = Message(
        created_at=datetime.now(timezone.utc).isoformat(),
        name="AI Assistant",
        role="assistant",
        content=answer,
    )

    zep_client.thread.add_messages(thread_id, messages=[assistant_msg])

    return answer

print("\n🤖 AI Agent Ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    reply = chat_with_agent(user_input)
    print("AI:", reply)