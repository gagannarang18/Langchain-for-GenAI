from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser   
from langchain.schema.runnable import RunnableParallel, RunnableLambda

load_dotenv()

prompt1= PromptTemplate(
    template="Generate a tweet about \n {topic}",
    input_variables=["topic"]
)

prompt2= PromptTemplate(
    template="Generate a Linkedin post about \n {topic}",
    input_variables=["topic"]
)

model=ChatGroq(model="llama-3.1-8b-instant")    

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        'tweet': prompt1|model|parser,
        'linkedin_post' : prompt2|model|parser
    }
)

result=parallel_chain.invoke({"topic": "AI"})

print(result['tweet'])
print(result['linkedin_post'])