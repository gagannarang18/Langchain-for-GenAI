from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

parser = JsonOutputParser()


model = ChatGroq(model="llama-3.1-8b-instant")

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Give me the name,age,city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={
        'format_instruction':parser.get_format_instructions()
    }
)

prompt=template1.format()
result=model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)
print(type(final_result))