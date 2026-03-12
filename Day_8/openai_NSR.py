from openai import OpenAI
import time

client = OpenAI()

start_time = time.time()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Write exactly 200 words explaining Artificial Intelligence"}
    ],
    temperature=0
)

end_time = time.time()

print(response.choices[0].message.content)

print("\nTotal Time (Non-Streaming):", round(end_time - start_time, 2), "seconds")