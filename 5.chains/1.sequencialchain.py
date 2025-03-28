from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model_hf=ChatHuggingFace(llm=llm)
model_google = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
parser=StrOutputParser()

prompt1=PromptTemplate(
    input_variables=['topic'],
    template="Generate a 5 line report on the topic {topic}"
)
prompt2=PromptTemplate(
    input_variables=['text'],
    template="Generate a 1 line summary from the following text. /n {text}"
)
chain= prompt1 | model_hf | parser | prompt2 | model_google | parser
result=chain.invoke({'topic': 'Unemployment in India'})

print(result)
# result-> India faces high unemployment due to structural issues, worsened by the pandemic, despite government efforts to boost skills and infrastructure.

# chain.get_graph().print_ascii() 
# above code is to display the graphical flow of execution that is done
