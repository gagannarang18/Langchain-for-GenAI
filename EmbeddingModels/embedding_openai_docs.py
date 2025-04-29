from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-ada-002",dimensions=32) 

docs=["Delhi is the capital of India",
      "Kolkata is the capital of West Bengal",
      "Mumbai is the capital of Maharashtra"]

result=embedding.embed_documents(docs)
print(str(result))