from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate



chat_template = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful customer support agent."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}")
        
    ]
)

chat_history=[]

#load chat history from file
with open("chat_history.txt", "r") as file:
    chat_history.extend(file.readlines())
    
print(chat_history)

#create prompt with chat history
prompt=chat_template.invoke({"chat_history": chat_history, "query":"Will you give my refund?"})

print(prompt)