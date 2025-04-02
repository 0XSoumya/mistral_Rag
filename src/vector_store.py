# Code for managing the vector database
import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

chroma_client = chromadb.PersistentClient(path="./data/chroma_db")
vectorstore = Chroma(client=chroma_client, embedding_function=OpenAIEmbeddings())
