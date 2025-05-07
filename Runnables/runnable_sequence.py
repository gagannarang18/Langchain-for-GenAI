from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from pydantic import BaseModel, Field

load_dotenv()

prompt= PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=["topic"]
)

parser=StrOutputParser()

model=ChatGroq(model="llama-3.1-8b-instant")

chain=RunnableSequence(prompt,model,parser)
result = chain.invoke({"topic": "cats"})
print(result)
chain.get_graph().print_ascii()