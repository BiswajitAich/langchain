from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)
prompt1=PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Explain the following joke: /n {text}',
    input_variables=['text']
)

joke_generation_chain=RunnableSequence(prompt1, model, parser)

parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

chain=RunnableSequence(joke_generation_chain, parallel_chain)

print(chain.invoke({'topic':'cricket'}))

# output -----------------------------------
# {'joke': 'Why did the cricket go to the doctor? \n\nBecause it was feeling a bit wicket! 😂 🏏 \n', 'explanation': 'This joke uses wordplay on the word "wicket." \n\n* **Normal meaning:** A wicket is a structure with two wooden pieces, usually made of planks, placed on a field to be a target for the bowlers on a cricket pitch.\n* **Joke meaning:**  "Wicket" in the joke sounds similar to "wicket", meaning it refers to a person feeling *pitiful or defeated.* \n\nTherefore, the cricket went to the doctor because it was feeling "a bit wicket", a nonsensical but humorous way of saying that the cricket is feeling unwell. \n\nThe humor comes from the childishly amusing contrast between the two meanings, and the use of "wicket" in a typical phrase associated with cricket.  \n\n\nLet me know if you\'d like another joke explanation! \n'}