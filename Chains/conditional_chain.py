from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model1= ChatGroq(model="llama-3.1-8b-instant")  
parser=StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal["positive", "negative"] = Field(description="Give the sentiment of the feedback")
    
parser2=PydanticOutputParser(pydantic_object=Feedback)


prompt1=PromptTemplate(
    template="Classify the following user's feedback text into positive or negative only. \n {feedback}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}  
)

classifier_chain=prompt1|model1|parser2

prompt2=PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)


branch_chain=RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2|model1|parser),    
    (lambda x:x.sentiment == 'negative', prompt3|model1|parser),
    RunnableLambda(lambda x: "could not find sentiment")
)


chain= classifier_chain | branch_chain

print(chain.invoke({"feedback": "The product is amazing and works perfectly!"}))
chain.get_graph().print_ascii()