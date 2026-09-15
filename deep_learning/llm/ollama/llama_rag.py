from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3", base_url="http://127.0.0.1:11434")

# print(llm.invoke("What is your name"))

print(llm.invoke("What is Amnya"))
