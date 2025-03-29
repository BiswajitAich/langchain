from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)
prompt=PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Explain the following joke: /n {text}',
    input_variables=['text']
)

chain=RunnableSequence(prompt, model, parser, prompt2, model, parser)
print(chain.invoke({'topic':'AI'}))






# output------------------------------------------
# This joke is playing on the stereotype of AI being good at processing and learning data, while humans struggle with it, especially in the grand scope of AI's multi-faceted development and learning capabilities.


# So here's the breakdown:

# * **AI versus Humans:** The joke sets up a basic contrast between Artificial intelligence, represented as "the AI," and humans, as the "learners".
# * **The "cross the road" act:**  This is a simple, familiar scenario.
# * **The punchline:** The AI's reason for crossing the road is  "To prove humans weren't the faster learners!",  which is funny because it plays on a big perceived differences between compatibility used to manifest AI and biological limitations humans have.

#  **Why is it funny?**

# * **Surprising answer:**  Instead of a logical or specific reason for AI to cross the road, the joke leans on a common human trait - a desire to playfully outsmarted others.
# * **Exaggerated difference:** We often emphasize AI's quick learning, while at the same time, we acknowledge our own, well, human learning.


# The joke is a humorous way to highlight a common trope: the humorous distance between human and AI learning. It uses wordplay and unexpected humor to make a casual comment.