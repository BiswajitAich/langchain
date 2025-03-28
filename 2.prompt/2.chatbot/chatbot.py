from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from huggingface_hub.errors import HfHubHTTPError
from dotenv import load_dotenv

load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)

history=[
    SystemMessage(content='Ypu are a helpful ai assistant')
]
while 1:
    userinput = input('You: ')
    history.append(HumanMessage(content=userinput))
    if userinput.lower()=='exit':
        break
    try:
        result = model.invoke(history)
        history.append(AIMessage(content=result.content))
        print(f"Ai: {result.content}")
    except HfHubHTTPError as e:
        print(e)
print("\n\n",history)