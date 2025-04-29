from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict,Annotated
load_dotenv()


model=ChatGroq(model="llama-3.1-8b-instant")

class Review(TypedDict):
    summary: Annotated[str,"A brief summary of the review"]
    sentiment: Annotated[str,"Return sentiment of the review either Positive or Negative"] #just for safer side we use annotated 
    
structured_model=model.with_structured_output(Review)

result=structured_model.invoke("I love this product!")
print(result)