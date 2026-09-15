from langchain_community.llms import Ollama

llm = Ollama(model="llama3", base_url="http://127.0.0.1:11434")

print(llm.invoke("What is your name"))
