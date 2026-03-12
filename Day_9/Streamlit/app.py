# Final 

import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

client = OpenAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})










# import streamlit as st
# from langchain_openai.chat_models import ChatOpenAI
# from dotenv import load_dotenv
# import os

# # Loads API Key 
# load_dotenv()

# st.title("🦜🔗 Quickstart App")


# def generate_response(input_text):
#     model = ChatOpenAI(temperature=0.7, api_key=os.getenv("OPENAI_API_KEY"))
#     st.info(model.invoke(input_text))


# with st.form("my_form"):
#     text = st.text_area(
#         "Enter text:",
#         "What are the three key pieces of advice for learning how to code?",
#     )
#     submitted = st.form_submit_button("Submit")

#     if submitted:
#         generate_response(text)
















# ====================================================================

# ## 7) OpenAI - Streaming - 

# import streamlit as st
# from openai import OpenAI

# client = OpenAI()

# st.title("Chatbot - LLM - Streaming")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("What is up?"):

#     st.session_state.messages.append({"role": "user", "content": prompt})

#     with st.chat_message("user"):
#         st.markdown(prompt)
    
#     with st.chat_message("assistant"):
#         placeholder = st.empty()
#         response = ""

#         stream = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=st.session_state.messages,
#             stream=True
#         )

#         for chunk in stream:
#             if chunk.choices[0].delta.content is not None:
#                 token = chunk.choices[0].delta.content
#                 response += token
#                 placeholder.markdown(response)

#     st.session_state.messages.append(
#         {"role": "assistant", "content": response}
#     )

# ===================================================================================

# ## 6) OpenAI - Streaming - more inputs

# import streamlit as st
# from openai import OpenAI

# client = OpenAI()

# st.title("Chatbot - LLM - Streaming")

# if "messages" not in st.session_state:
#     st.session_state.messages = list()

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])


# if prompt := st.chat_input("What is up?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):

#         stream = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=st.session_state.messages,
#             stream=True
#         )

#         full_response = st.write_stream(
#             chunk.choices[0].delta.content or ""
#             for chunk in stream
#         )

#     st.session_state.messages.append(
#         {"role": "assistant", "content": full_response}
#     )


# ====================================================================

# ## 5) OpenAI - Streaming

# import streamlit as st
# from openai import OpenAI

# client = OpenAI()

# st.title("Chatbot - LLM - Streaming")

# if "messages" not in st.session_state:
#     st.session_state.messages = list()

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# prompt = st.chat_input("Ask something...")

# if prompt:

#     st.session_state.messages.append({"role": "user", "content": prompt})

#     with st.chat_message("user"):
#         st.markdown(prompt)
    
#     with st.chat_message("assistant"):
#         placeholder = st.empty()
#         response = ""

#         stream = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=st.session_state.messages,
#             stream=True
#         )

#         for chunk in stream:
#             if chunk.choices[0].delta.content is not None:
#                 token = chunk.choices[0].delta.content
#                 response += token
#                 placeholder.markdown(response)

#     st.session_state.messages.append(
#         {"role": "assistant", "content": response}
#     )
# =======================================================

# ## 4) OpenAI - Non Streaming - history to LLM

# import streamlit as st
# from openai import OpenAI

# client = OpenAI()

# st.title("Chatbot - LLM - Non Streaming - with History")

# if "messages" not in st.session_state:
#     st.session_state.messages = list()

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# prompt = st.chat_input("Ask something...")

# if prompt:
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     with st.chat_message("user"):
#         st.markdown(prompt)
    
#     response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=st.session_state.messages)

#     assistant_reply = response.choices[0].message.content

#     with st.chat_message("assistant"):
#         st.markdown(assistant_reply)

#     st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

# ============================================================================================

# ## 3) OpenAI - Non Streaming - no history to LLM

# import streamlit as st
# from openai import OpenAI

# client = OpenAI()

# st.title("Chatbot - LLM - Non Streaming - Without History")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# prompt = st.chat_input("Ask something...")

# if prompt:

#     st.session_state.messages.append({"role": "user", "content": prompt})

#     with st.chat_message("user"):
#         st.markdown(prompt)
    
#     response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": prompt}
#     ])

#     assistant_reply = response.choices[0].message.content

#     with st.chat_message("assistant"):
#         st.markdown(assistant_reply)

#     st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

# ==========================================================================================

# ## 2) Basic with Session State

# import streamlit as st

# st.title("Chatbot - with Session State")

# # Initialize chat history -- Session State -- It behaves like a Python dictionary that persists across reruns.
# if "messages" not in st.session_state:
#     st.session_state.messages = list()

# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # User input
# prompt = st.chat_input("Ask something...")

# if prompt:
#     # Store user message - instanly after the prompt is given
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     # Display user message
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Assistant reply
#     response = "This is a test response."
#     with st.chat_message("assistant"):
#         st.markdown(response)

#     st.session_state.messages.append({"role": "assistant", "content": response})

# ======================================================================================================

# ## 1) Basic Implementation - Without session state

# import streamlit as st

# st.title("Basic Chatbot")

# # User input
# prompt = st.chat_input()

# if prompt:
#     # Display user message
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Fake assistant reply
#     response = "This is a test response."
#     with st.chat_message("assistant"):
#         st.markdown(response)