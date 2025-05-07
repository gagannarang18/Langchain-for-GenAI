from langchain.schema.runnable import RunnableLambda, RunnablePassthrough, RunnableSequence
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser   
from langchain.schema.runnable import RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableSequence

load_dotenv()

def word_counter(text):
    """Counts the number of words in a text."""
    return len(text.split())

prompt1= PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=["topic"]
)

model=ChatGroq(model="llama-3.1-8b-instant")
parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter)
}
)

final_chain=RunnableSequence(
    joke_gen_chain,
    parallel_chain
)

result=final_chain.invoke({"topic": "cats"})

final_result=""" {} \n word-count: {}""".format(result['joke'], result['word_count'])
print(final_result)