from langchain_community.document_loaders import WebBaseLoader,PyPDFLoader

url="https://www.amazon.in/deals?ref_=nav_cs_gb"

loader=WebBaseLoader(url)

docs = loader.load()

print(len(docs)) # Number of documents loaded
print(docs[0].page_content) # Content of the first document
