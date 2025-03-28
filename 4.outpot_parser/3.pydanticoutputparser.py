from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str=Field(description='Name of the person')
    age: int=Field(description='Age of the person', gt=18, lt=70)
    gender: Literal['M', 'F', 'O']=Field(description='Gender of the person male or female or other')
    city: str=Field(description='Name the city of the person belongs to')

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='Generate a name, age, gender, and city of a fictional person who lives in {country} /n {format_instruction}' ,
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain= template | model | parser
result=chain.invoke({'country': 'India'})

print(result)
# result-> name='Raunak Jain' age=28 gender='M' city='Bangalore'
