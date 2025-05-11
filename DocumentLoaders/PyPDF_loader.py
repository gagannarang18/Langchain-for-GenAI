from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq

loader=PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()    

print(len(docs)) # Number of documents loaded

print(docs[0].page_content) # Content of the first document
print(docs[0].metadata) # Metadata of the first document