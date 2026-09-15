import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv(dotenv_path=".env")

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

models = client.models.list()

for m in models:
    print(m.id)

resp = client.responses.create(model="gpt-4o-mini", input="Hi, what is your version?")

print("OpenAI Response:", resp.text)

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Tell me something interesting about robotics."}
    ],
)
print(resp.text)
