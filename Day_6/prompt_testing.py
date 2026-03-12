# ====================== PROMPT EXPERIMENTATION ======================

from google import genai
import os
from dotenv import load_dotenv
import pandas as pd

# Load API key
load_dotenv()

# Create Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ------------------- Prompt Dictionary -------------------

prompts_to_test = {
    "Standard": "Why is the sky blue?",

    "Persona": "You are a Victorian-era poet. Explain to a curious child why the sky is blue using flowery, romantic language and metaphors.",
    
    "Chain-of-Thought": "Explain why the sky is blue. First, define Rayleigh scattering. Second, explain how the Earth's atmosphere interacts with different wavelengths of light. Third, explain why the sky appears blue rather than violet.",
    
    "Constraint-Based": "Explain why the sky is blue. Use exactly two sentences. You are forbidden from using the words 'sun' or 'color'.",
    
    "Few-Shot": "Q: Why is grass green? A: Chlorophyll absorbs red/blue light and reflects green. \nQ: Why is the ocean blue? A: Water molecules absorb long-wave reds and scatter blues. \nQ: Why is the sky blue? A: "    
}

# ------------------- Empty Lists -------------------

technique_list = []
prompt_list = []
response_list = []

# ------------------- Loop Through Prompts -------------------

for technique, prompt in prompts_to_test.items():

    response = client.models.generate_content(
        model="gemma-3-1b-it",
        contents=prompt,
    )

    technique_list.append(technique)
    prompt_list.append(prompt)
    response_list.append(response.text)

# ------------------- Create DataFrame -------------------

df = pd.DataFrame({
    "Technique": technique_list,
    "Prompt": prompt_list,
    "Response": response_list
})

# ------------------- Save For Documentation -------------------

df.to_json("prompt_experimentation.json", orient="records", indent=4)