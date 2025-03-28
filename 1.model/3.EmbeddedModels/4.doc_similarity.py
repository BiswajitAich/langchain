from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='', dimensions=000)
documents = [
    "......",
    "......",
    "......"
]
query = "user question??????"

doc_emb = embedding.embed_documents(documents)
q_emb = embedding.embed_query(query)

scores = cosine_similarity([q_emb], doc_emb)[0]
index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]
print(documents[index])
print('Similarity score is: ', score)