from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Generate a linkedin post about topic {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1, model, parser),
    'linkedin':RunnableSequence(prompt2, model, parser)
})
result=parallel_chain.invoke({'topic':'AI'})

print('TWEET:\t',result['tweet'])
print('\n\n')
print('LINKEDIN:\t',result['linkedin'])
'''
TWEET:   🤯 AI is revolutionizing so many industries! Imagine personalized learning, even better healthcare & self-driving cars. It's changing the way we live & work, and the possibilities are only growing! Let's embrace the future together! 🚀 #AI #Tech #Innovation #Future isNow 




LINKEDIN:        ##  The Future of Work is Here:  AI is Transforming Industries 🤖 

The integration of Artificial Intelligence (AI) is no longer a futuristic concept, it's a present reality, and it's having a profound impact across industries.  🚀

Just think about it - from automating tedious tasks to powering hyper-personalized experiences, AI holds the key to unlocking unprecedented efficiency and innovation. 💡

Here are some key trends driving this transformation:

* **Hyper-Personalized Customer Experiences:** AI is enabling businesses to deliver tailored messages, products, and services, enhancing customer satisfaction and driving revenue growth.
* **Improved Operations and Productivity:** From smart inventory management to predictive maintenance, AI is streamlining processes and boosting operational efficiency.
* **Data-Driven Decisions:** AI algorithms can analyze massive datasets to extract insights, uncovering crucial trends and enabling more informed business decisions.

👉  I'm excited to see how AI continues to reshape the future of work!  How has AI impacted your business or allowed you to enhance your professional journey?

#AI #artificialIntelligence #innovation #futureofwork #businesstechnology #digitailization

---
**(Add a relevant image or video to your post - a news image/graphic about AI in a specific industry, or even something illustrating how AI is being used in a workplace setting)**
'''