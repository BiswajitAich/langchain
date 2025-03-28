from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model='gpt-4')#temperture=...(0 to 2), max_completion_tokens=...(max token length)
result = model.invoke("what is the capital of India?")
print(result.content)