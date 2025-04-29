from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful {domain} expert."),
        ("human", "Explain what is {topic} in simple words."),
    ]
)

prompt=chat_template.invoke({'domain':"AI", 'topic':"Langchain"})
print(prompt)