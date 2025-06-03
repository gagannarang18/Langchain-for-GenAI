from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loaader= PyPDFLoader("dl-curriculum.pdf")

docs= loaader.load()

splitter= CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=0
)

result=splitter.split_documents(docs)

print(result[0])

##chunk overlap helps to avoid losing context between chunks