import os
from google.genai import Client
from dotenv import load_dotenv

# Load .env file
load_dotenv(dotenv_path=".env")

gemini_api_key = os.getenv("GOOGLE_API_KEY")
# openai_api_key = os.getenv("OPENAI_API_KEY")

client = Client(api_key=gemini_api_key)

models = client.models.list()

for m in models:
    print(m.name)

resp = client.models.generate_content(
    model="gemini-3.8-flash", contents="Hi, what is your version?"
)

print("Gemini Response:", resp.text)

resp = client.chat.send_message(
    model="gemini-3.8-flash", messages="Tell me something interesting about robotics."
)
print(resp.text)
