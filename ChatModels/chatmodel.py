from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv

model=ChatOpenAI(model="gpt-4",temperature= 0.5,max_completion_tokens=100)
result=model.invoke("What is the capital of India?")
print(result.content)

##chatmodels take input as a string but their output contains many things , not just a string.Thats why we are just using result.content to fetch our answer.