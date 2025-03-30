from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")
model = ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='Summmarise the product from the text: \n {text} ',
    input_variables=['text']
)
parser=StrOutputParser()

url='https://lilastore.vercel.app/earrings/fancy-earring/1'
loader=WebBaseLoader(web_path=url)

docs=loader.load()

chain=prompt | model | parser
result=chain.invoke({'text': docs[0].page_content})
print(docs[0].page_content)
print('\n\n')
print(result)
