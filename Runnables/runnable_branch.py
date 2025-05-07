from langchain.schema.runnable import RunnableLambda, RunnablePassthrough, RunnableSequence
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser   
from langchain.schema.runnable import RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableSequence

load_dotenv()

