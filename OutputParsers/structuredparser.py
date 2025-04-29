from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()


model = ChatGroq(model="llama-3.1-8b-instant")

schema=[
    ResponseSchema(name='fact_1', description='fact  1 about the topic'),
    ResponseSchema(name='fact_1', description='fact  1 about the topic'),
    ResponseSchema(name='fact_1', description='fact  1 about the topic')
]

parser=StructuredOutputParser.from_response_schemas(schema) 

template=PromptTemplate(
    template='Give me 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={
        'format_instruction':parser.get_format_instructions()
    }
)
    
chain=template | model | parser
result = chain.invoke({'topic':'black hole'}) 
print(result)