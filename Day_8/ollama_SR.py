import ollama
import time

start_time = time.time()

stream = ollama.chat(
    model='phi',
    messages=[
        {'role': 'user', 'content': 'Write exactly 200 words explaining Artificial Intelligence.'}
    ],
    stream=True
)

first_token_time = None

for chunk in stream:
    if first_token_time is None:
        first_token_time = time.time()
    print(chunk['message']['content'], end='', flush=True)

end_time = time.time()

print("\n\nTime to First Token:", round(first_token_time - start_time, 2), "seconds")
print("Total Time (Streaming):", round(end_time - start_time, 2), "seconds")







# import ollama

# stream = ollama.chat(
#     model='phi',
#     messages=[
#         {'role': 'user', 'content': 'Explain Streaming in LLM in 5 lines'}
#     ],
#     stream=True
# )

# for chunk in stream:
#     print(chunk['message']['content'], end='', flush=True)