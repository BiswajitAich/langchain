from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")
model = ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='Write a precise summary of the text: /n {text}',
    input_variables=['text']
)
parser=StrOutputParser()

loader=TextLoader(file_path='Story.txt', encoding='utf-8')
docs=loader.load()
print(docs)

chain=prompt | model | parser
result=chain.invoke({'text':docs[0].page_content})

print('\n\n')
print(result)


# output -----------------------------------
'''
[Document(metadata={'source': 'Story.txt'}, page_content='The Hidden Library\nEmma had always been fascinated by old books. One evening, while exploring her grandmother’s attic, she stumbled upon a dusty wooden door she had never noticed before. Intrigued, she pushed it open and found herself in a dimly lit library filled with ancient tomes and handwritten scrolls.\n\nAs she ran her fingers along the spines of the books, she noticed one that stood out—a deep blue leather-bound volume with no title. She opened it, and the words inside began to glow. The book whispered secrets of lost civilizations, forgotten spells, and the mysteries of time itself.\n\nEmma realized this wasn’t just any library. It was a gateway to knowledge long buried by history. And she was its new keeper.\n')]



While exploring her grandmother's attic, Emma discovers a hidden, magical library filled with ancient texts.  One unmarked blue book, glowing with secrets, attracts her attention leading her to realize the library is a gateway to forgotten wisdom, and she is its designated caretaker.
'''