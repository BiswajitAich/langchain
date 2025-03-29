from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")
model = ChatHuggingFace(llm=llm)


joke_prompt = PromptTemplate(template="Write a joke on {topic}", input_variables=["topic"])
explanation_prompt = PromptTemplate(
    template="Explain the following joke: /n {text}", input_variables=["text"]
)

parser = StrOutputParser()


def word_count(text):
    return len(text.split())

joke_chain = RunnableSequence(joke_prompt, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(explanation_prompt, model, parser),
        "joke_word_count": RunnableLambda(word_count),
    }
)

chain = RunnableSequence(joke_chain, parallel_chain)

print(chain.invoke({"topic": "ai"}))

# output----------------
# {
#   'joke': "Why don't AI's like to go to parties? \n\nBecause they're always afraid of getting into a *data* frenzy! 😅 \n", 
#   'explanation': 'The joke uses wordplay combining the concepts of AI and social interaction with a pun on  "data" \n\n* **AI\'s and Data:**  Artificial intelligence (AI) constantly "processes" and "analyzes" data to learn and produce outputs. This data is considered one of its engines for "thinking."\n\n* **Data Frenzy:** A "data frenzy" is not what you might associate with a social gathering, but it creates the same effect as other usage; overwhelming. \n\nThe joke implies that AI, being driven by data, would get overwhelmed in social situations due to the volume of information and interactions, hence the humor arises from the unexpected and unexpected connection between these two things. \n', 
#   'joke_word_count': 19
# }