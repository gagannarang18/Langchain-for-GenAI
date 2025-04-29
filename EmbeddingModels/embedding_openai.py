from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model="text-embedding-ada-002",dimensions=32) 
result=embedding.embed_query("Delhi is the capital of India")
print(str(result))