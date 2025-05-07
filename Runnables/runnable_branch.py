from langchain.schema.runnable import RunnableLambda, RunnablePassthrough, RunnableSequence
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableSequence,RunnableBranch
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser

load_dotenv()


class Feedback(BaseModel):

    sentiment: Literal['Spam', 'Non-Spam'] = Field(description='Give the sentiment of the mail text')

parser = PydanticOutputParser(pydantic_object=Feedback)


model=ChatGroq(model="llama-3.1-8b-instant")
parser2=StrOutputParser()


prompt1= PromptTemplate(
    template="  Classify the following email text into Spam or Non-Spam {text} \n {format_instruction}",
    input_variables=["text"],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

classifier_chain = RunnableSequence(prompt1,model,parser)

prompt2 = PromptTemplate(
    template='Write an appropriate response to this Spam Mail \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this Non-Spam Mail \n {text}',
    input_variables=['text']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Spam', prompt2 | model | parser2),
    (lambda x:x.sentiment == 'Non-Spam', prompt3 | model | parser2),
    RunnableLambda(lambda x: "could not find sentiment")
)

final_chain=RunnableSequence(
    classifier_chain,
    branch_chain
)

result=final_chain.invoke({"text": "This is a spam email"})
print(result)

