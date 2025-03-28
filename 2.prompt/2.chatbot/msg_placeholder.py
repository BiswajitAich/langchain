from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer support ai agent and the company name is "XYZ"'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

# load chat history
chat_history=[]
with open('prompt/2.chatbot/chat_history.txt') as f:
    chat_history.extend(f.readlines())

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'I have an issue with my order number 12345.'})
print(prompt)
