from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls="PyPDFLoader",
)

docs= loader.load()

print(len(docs)) # Number of documents loaded(total no. of pages)

#in books directory, you can add your pdfs and try riunning this  code.
# print(docs[0].page_content) # Content of the first document