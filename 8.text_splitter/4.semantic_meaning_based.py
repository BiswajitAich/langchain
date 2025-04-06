# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# from langchain_experimental.text_splitter import SemanticChuncker
# load_dotenv()

# text_splitter=SemanticChuncker(
#     OpenAIEmbeddings(), 
#     breakpoint_threshold_type="standard_deviation",
#     breakpoint_threshold_amount=1
# )
# sample="""

# """
# docs = text_splitter.create_documents({sample})
# print(docs)