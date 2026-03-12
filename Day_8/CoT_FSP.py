from openai import OpenAI

client = OpenAI()

print('Normal Prompting')

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", 
         "content": """The cafeteria had 23 apples. 
                        They used 20 to make lunch and then bought 6 more. 
                        How many apples do they have now?"""}
    ],
    temperature=0
)

print(response.choices[0].message.content)
print("=" * 70)

print('Few-Shot Prompting')

fsp_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", 
         "content": """ Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
                        A: The answer is 11.
                        Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?
                        A: """}
    ],
    temperature=0
)

print(fsp_response.choices[0].message.content)
print("=" * 70)

print('Chain of Thought Prompting')

cot_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", 
         "content": """ Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?
                        Show how you derive the answer step by step."""}
    ],
    temperature=0
)

print(cot_response.choices[0].message.content)
print("=" * 70)

print('Few Shot CoT Prompting')

fs_cot_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", 
         "content": """ Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
                        A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11.
                        Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?
                        A: """}
    ],
    temperature=0
)

print(fs_cot_response.choices[0].message.content)