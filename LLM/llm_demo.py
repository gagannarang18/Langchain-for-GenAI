from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm =OpenAI(model="gpt-3.5-turbo-instruct") # Replace with your OpenAI API key

result=llm.invoke("What is the capital of India?")

print(result) 


##llms take input as a string and give output as a string