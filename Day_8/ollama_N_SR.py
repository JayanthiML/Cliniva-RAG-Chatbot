import ollama
import time

start_time = time.time()

response = ollama.chat(
    model='phi',
    messages=[
        {'role': 'user', 'content': 'Write exactly 200 words explaining Artificial Intelligence.'}
    ]
)

end_time = time.time()
print(response['message']['content'])
print("\nTotal Time (Non-Streaming):", round(end_time - start_time, 2), "seconds")







# import ollama

# response = ollama.chat(
#     model='phi',
#     messages=[
#         {'role': 'user', 'content': 'Explain Streaming in LLM in 5 lines'}
#     ]
# )

# print(response['message']['content'])