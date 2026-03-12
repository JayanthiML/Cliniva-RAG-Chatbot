from google import genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Create Gemini Client
# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )

# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents="How does LLM Work?",
# )
# print(response.text)

from google import genai
import os
from dotenv import load_dotenv

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
for model in client.models.list():
    print(f"Model Name: {model.name} | Supported Methods: {model.supported_actions}")