from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant")


messages=[
    SystemMessage(content="You are a helpful assistant."), 
    HumanMessage(content="Tell me about Langchain")]


result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)