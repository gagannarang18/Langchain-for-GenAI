from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq

loader=PyPDFLoader("sample.pdf")
docs = loader.load()    