from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model_hf=ChatHuggingFace(llm=llm)
model_google = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
parser=StrOutputParser()

prompt_notes=PromptTemplate(
    template='Generate short and simple notes on the following text. /n {text}',
    input_variables=['text']
)
prompt_quiz=PromptTemplate(
    template='Generate 5 short question answers from the following text. /n {text}',
    input_variables=['text']
)
prompt=PromptTemplate(
    template='Merge the provided notes and quiz into a single document. /n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parallel_chain=RunnableParallel({
    'notes': prompt_notes | model_google | parser,
    'quiz': prompt_quiz | model_hf | parser
})
merge_chain=prompt | model_hf | parser
# merge_chain=prompt | model_google | parser # It will work same as above line

chain=parallel_chain | merge_chain

text="""
LangChain is an open source framework for building applications based on large language models (LLMs). LLMs are large deep-learning models pre-trained on large amounts of data that can generate responses to user queries—for example, answering questions or creating images from text-based prompts. LangChain provides tools and abstractions to improve the customization, accuracy, and relevancy of the information the models generate. For example, developers can use LangChain components to build new prompt chains or customize existing templates. LangChain also includes components that allow LLMs to access new data sets without retraining.
"""
result=chain.invoke({'text':text})
print(result)

# chain.get_graph().print_ascii() 
# above code is to display the graphical flow of execution that is done




# result ->

## LangChain: Enhancing LLM-based Applications

# **What is LangChain?**

# LangChain is an open-source framework designed to streamline the development of applications using Large Language Models (LLMs). It empowers developers to build more efficient, accurate, and highly-relevant LLM-powered applications by enabling customization, refinement, and tailored data access.

# **Key Features of LangChain:**

# * **Prompt Chaining:** Allows developers to build complex chains of instructions for LLMs, improving response flow and coherence.
# * **Template Customization:** Provides components for modifying and tailoring LLM responses, giving more control over content generation.
# * **External Data Access:** Enables LLMs to leverage external data sets without needing to be retraining, simplifying integration with databases or APIs.

# **How does LangChain improve LLM performance?**

# LangChain enhances LLM performance through:

# * **Customization:** Allowing developers to fine-tune how LLMs respond based on specific needs and goals.
# * **Accuracy:** Ensuring responses are relevant to the task and information.
# * **Relevancy:** Optimizing the generated responses for focused target information.

# Additionally, LangChain simplifies the development process by offering components for building complex chains of instructions and customizing templates, ultimately streamlining the development and integration of LLM-based applications.

# **Example Use Cases of LangChain:**

# * **Chatbots:** Tailoring the chat experience with interactive responses aligned to specific conversations.
# * **Text Generation & Editing:** Enhancing creative content generation and refinement.
# * **Question Answering & Summarizing:** Generating accurate and efficient answers based on various data sources.


#  **Summary**

# LangChain provides a powerful suite of tools for developers building applications leveraging the capabilities of LLMs like ChatGPT. By offering tools for customization, template manipulation, and external data access, LangChain allows for the creation of more sophisticated and accurate LLM-powered applications.
