from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenAI(model="chat-bison",temperature= 0.5,max_completion_tokens=100)    
result=model.invoke("What is the capital of India?")
print(result.content)