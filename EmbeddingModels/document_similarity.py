from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-ada-002", dimensions=300)

docs = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Mumbai is the capital of Maharashtra"
]

docs_embeddings = embedding.embed_documents(docs)


query="tell me about the capital of India"
query_embedding = embedding.embed_query(query)


scores=cosine_similarity([query_embedding], docs_embeddings)[0]

index,score=print(sorted(list(enumerate(scores)),key=lambda x: x[1])[-1])

print(docs[index])

print("the similarity score is ",score)