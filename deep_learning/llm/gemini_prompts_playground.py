from google.genai import Client
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = Client(api_key=api_key)

# Use a supported model from your list
model = "models/gemini-2.5-flash"

response = client.models.generate_content(
    model=model, contents="Explain Neuron in Neural Networks for deep learning?"
)

print(response.text)
