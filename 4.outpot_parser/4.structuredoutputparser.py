from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='point_1_positive', description='point 1, a positive point of the topic'),
    ResponseSchema(name='point_2_positive', description='point 2, a positive point of the topic'),
    ResponseSchema(name='point_1_negative', description='point 1, a negative point of the topic'),
    ResponseSchema(name='point_2_negative', description='point 2, a negative point of the topic')
]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    input_variables=['movie_name'],
    partial_variables={'format_instruction': parser.get_format_instructions()},
    template="Give 2 positive and 2 negative points of the movie {movie_name} /n {format_instruction}"
)
chain= template | model | parser
result=chain.invoke({'movie_name': 'Avatar 2'})

print(result)
# result-> {'point_1_positive': 'The movie boasts stunning visual effects and a rich, immersive world.', 'point_2_positive': 'The underwater setting and aquatic life in the film are incredibly captivating.', 'point_1_negative': 'Some viewers felt the film dragged on, with a slow pace and reliance on exposition.', 'point_2_negative': "The pacing and the plot structure themselves weren't satisfying to everyone, leading to a sense of redundancy and repetitive elements."}
