from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model_hf=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative']=Field(description='Give the sentiment of the feedback result as positive or negative')
parser2=PydanticOutputParser(pydantic_object=Feedback)


prompt1=PromptTemplate(
    template='Classify the statement of the following feedback text into positive or negative. /n {feedback} /n {feedback_instruction}',
    input_variables=['feedback'],
    partial_variables={'feedback_instruction':parser2.get_format_instructions()}
)
classifier_chain=prompt1 | model_hf | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate, empathetic, and helpful response to the following positive feedback. '
             'Address the specific issues mentioned and suggest actionable improvements. '
             '/n Feedback: {feedback}',
    input_variables=['feedback'],
)

prompt3 = PromptTemplate(
    template='Write an appropriate, empathetic, and helpful response to the following negative feedback. '
             'Address the specific issues mentioned and suggest actionable improvements. '
             '/n Feedback: {feedback}',
    input_variables=['feedback'],
)

branch_chain=RunnableBranch(
    # {condition, chain}
    (lambda x:x.sentiment == 'positive', prompt2 | model_hf | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model_hf | parser),
    RunnableLambda(lambda x: 'could not find sentiment')
)

chain=classifier_chain | branch_chain
result=chain.invoke({'feedback':"The website is so confusing! I couldn't find the product I was looking for, and the checkout process took forever.  Plus, the customer service rep I spoke with was unhelpful and rude."})

print(result)

# chain.get_graph().print_ascii() 
# above code is to display the graphical flow of execution that is done



# result->
# Please provide the negative feedback so I can give you a personalized and helpful response. 😊 

# Once you give me the feedback, I'll create an empathetic, actionable response that addresses:

# * **The specific issues raised.**
# * **Concrete suggestions for improvement.**
# * **A positive and supportive tone.**

# I look forward to helping! 💪