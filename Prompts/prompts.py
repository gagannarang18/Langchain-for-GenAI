from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model=ChatGroq(model="llama-3.1-8b-instant")

st.header("Research Tool")

paper_input=st.selectbox("Select a Research Paper:", ["Attention is all you need", "BERT: pre Training of Deep Bidirectional Transformers", "Diffusuion Models beats GANs on Image Synthesis"])
style_input=st.selectbox("Select Explaination style:", ["Beginner Friendly", "Mathematical", "Code-Oriented","Technical"])
length_input=st.selectbox("Select Explaination Length:", ["Short(1-2 paragarphs)", "Medium(3-5 paragraphs)", "Long(detailed explaination)"])

template=load_prompt("template.json") #load the prompt template from the json file

#fill the placeholders with the inputs given by the user
# prompt=template.invoke({"paper_input":paper_input, "style_input":style_input, "length_input":length_input})

if st.button("Summarize"):
    chain=template | model #create a chain using the prompt and model(chain method no need to invoke both model and temlate)
    result=chain.invoke({"paper_input":paper_input, "style_input":style_input, "length_input":length_input}) #invoke the chain with the inputs
    st.write(result.content)