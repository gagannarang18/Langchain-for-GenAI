from langchain_community.document_loaders import CSVLoader

loader=CSVLoader("Social_Network_Ads.csv")

docs = loader.load()

print(len(docs)) 

#for every row , there will be a document created.
print(docs[0].page_content) # Content of the first document