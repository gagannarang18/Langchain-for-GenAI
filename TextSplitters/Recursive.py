from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loaader= PyPDFLoader("dl-curriculum.pdf")

docs= loaader.load()

splitter= RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0
)

result=splitter.split_documents(docs)

print(result[4])

##chunk overlap helps to avoid losing context between chunks