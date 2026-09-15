import gradio as gr
import ollama

from bs4 import BeautifulSoup as bs
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

url = "https://en.wikipedia.org/wiki/Amnya_complex"
loader = WebBaseLoader(url)
documents = loader.load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# texts = text_splitter.split_documents(documents)
# embeddings = OllamaEmbeddings()
# vectorstore = Chroma.from_documents(texts, embeddings)
