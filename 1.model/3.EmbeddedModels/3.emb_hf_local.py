from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name='sentense-transformer/all-MiniLLLM-L6-v2')

text="........."
# documents = [
#     "statement 1 ...",
#     "statement 2 ...",
#     "..............."
# ]

vector=embedding.embed_query(text)
# vector=embedding.embed_documents(documents)
print(vector)