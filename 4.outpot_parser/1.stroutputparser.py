from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)
template1=PromptTemplate(
    input_variables=["topic"],
    template="write a detailed report on {topic}"
)
template2=PromptTemplate(
    input_variables=["text"],
    template="write a 2 line summery on the following text. /n {text}"
)

# -----------------------------------------------------------------------
# prompt1=template1.invoke({'topic': 'black hole'})
# result=model.invoke(prompt1)
# prompt2=template2.invoke({'text': result.content})
# result1=model.invoke(prompt2)
# print(result1.content)
# -----------------------------------------------------------------------

parser=StrOutputParser()
chain=template1 | model | template2 | model | parser

result=chain.invoke({'topic':'black hole'})
print(result)
# result-> Black holes are regions of spacetime with such strong gravity that they trap everything, even light. Studying these extremly dense objects provides clues about the universe's fundamental laws and helps us understand how galaxies evolve.
