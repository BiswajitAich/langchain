from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

model = "sentence-transformers/paraphrase-MiniLM-L3-v2"
hf = HuggingFaceEmbeddings(model_name=model)

documents = [
    Document(
        page_content="My name is Biswajit Aich. I'm 22 years old and currently live in West Bengal, India.",
        metadata={"category": "personal", "importance": "high"},
    ),
    Document(
        page_content="I am studying B.Tech in Computer Science and Engineering at Academy of Technology. My expected graduation is in 2026.",
        metadata={"category": "education", "importance": "high"},
    ),
    Document(
        page_content="My technical skills include Python, JavaScript, React, TensorFlow, and PyTorch. I'm particularly interested in Natural Language Processing and Machine Learning applications.",
        metadata={"category": "skills", "importance": "high"},
    ),
    Document(
        page_content="I have previously interned at ABC Technologies where I worked on developing a recommendation system using collaborative filtering techniques.",
        metadata={"category": "experience", "importance": "medium"},
    ),
    Document(
        page_content="Currently, I'm practicing LangChain for building conversational AI systems and exploring vector databases for efficient information retrieval.",
        metadata={"category": "current_activity", "importance": "high"},
    ),
    Document(
        page_content="My final year project focuses on developing a question-answering system that can reason over multiple documents.",
        metadata={"category": "projects", "importance": "medium"},
    ),
    Document(
        page_content="In my free time, I enjoy playing chess, reading science fiction novels, and doing some paintings or sketches.",
        metadata={"category": "hobbies", "importance": "low"},
    ),
    Document(
        page_content="My career goal is to become a machine learning engineer specializing in large language models and multimodal AI systems.",
        metadata={"category": "goals", "importance": "medium"},
    ),
]

vectorStore = Chroma.from_documents(
    documents=documents, embedding=hf, collection_name="my_collection"
)

retriever = vectorStore.as_retriever(search_type='mmr', search_kwargs={"k": 2, "lambda_mult": 0.5})

query = "What is my name?"
result = retriever.invoke(query)

for i, doc in enumerate(result):
    print(f"\nResult {i+1}:")
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")



'''
Result 1:
Content: My name is Biswajit Aich. I'm 22 years old and currently live in West Bengal, India.
Metadata: {'category': 'personal', 'importance': 'high'}

Result 2:
Content: In my free time, I enjoy playing chess, reading science fiction novels, and doing some paintings or sketches.
Metadata: {'importance': 'low', 'category': 'hobbies'}
'''