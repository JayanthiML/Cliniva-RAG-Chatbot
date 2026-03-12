from openai import OpenAI
import time

client = OpenAI()

start_time = time.time()

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Write exactly 200 words explaining Artificial Intelligence"}
    ],
    temperature=0,
    stream=True
)

first_token_time = None

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        if first_token_time is None:
            first_token_time = time.time()
        print(chunk.choices[0].delta.content, end="", flush=True)

end_time = time.time()

print("\n\nTime to First Token:", round(first_token_time - start_time, 2), "seconds")
print("Total Time (Streaming):", round(end_time - start_time, 2), "seconds")









# from openai import OpenAI
# client = OpenAI()

# stream = client.responses.create(
#     model="gpt-5",
#     input=[
#         {
#             "role": "user",
#             "content": "Say 'double bubble bath' ten times fast.",
#         },
#     ],
#     stream=True,
# )

# for event in stream:
#     print(event)