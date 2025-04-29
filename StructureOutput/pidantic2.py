from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict,Annotated
from pydantic import BaseModel, Field,EmailStr
load_dotenv()


model=ChatGroq(model="llama-3.1-8b-instant")

class Review(BaseModel):
    summary: str=Field(description="A brief summary of the review")
    sentiment: str=Field(description="Return sentiment of the review either Positive or Negative") 
    
structured_model=model.with_structured_output(Review)

result=structured_model.invoke("I love this product!")
print(result.summary)#pydantic format of fetching certain thing value from the result
print(result.sentiment) #pydantic format of fetching certain thing value from the result