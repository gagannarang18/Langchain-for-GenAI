from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1= ChatGroq(model="llama-3.1-8b-instant")
model2= ChatGroq(model="llama-3.3-70b-versatile")

prompt1=PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)


prompt2=PromptTemplate(
    template="Generate 5 short question answers from the following text \n {text}",
    input_variables=['text']
)

prompt3=PromptTemplate(
    template="Merge the provided note and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes','quiz']
    
)

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        'notes': prompt1|model1|parser,
        'quiz' : prompt2|model2|parser
    }
)




