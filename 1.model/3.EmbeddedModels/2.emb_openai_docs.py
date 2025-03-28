from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='', dimensions=32)
documents = [
    "statement 1 ...",
    "statement 2 ...",
    "..............."
]
result = embedding.embed_documents(documents)
print(result)