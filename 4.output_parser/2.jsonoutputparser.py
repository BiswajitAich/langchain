from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template=PromptTemplate(
    input_variables=['movie_name'],
    partial_variables={'format_instruction': parser.get_format_instructions()},
    template="Give me the main actors name, director name and year of release data of the movie {movie_name} /n {format_instruction}"
)
chain= template | model | parser
result=chain.invoke({'movie_name': 'Avatar 2'})

print(result)
# result-> {'main_actors': 'Sam Worthington, Zoe Saldaña, Sigourney Weaver', 'director': 'James Cameron', 'release_year': 2022}