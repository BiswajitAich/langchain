from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableBranch,
    RunnablePassthrough
)

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")
model = ChatHuggingFace(llm=llm)


prompt1 = PromptTemplate(template="Write a short report on {topic}", input_variables=["topic"])
prompt2 = PromptTemplate(
    template="Summarize the following text: /n {text}", input_variables=["text"]
)

parser = StrOutputParser()


def word_count(text):
    return len(text.split())

report_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

chain = RunnableSequence(report_chain, branch_chain)

print(chain.invoke({"topic": "Economic situation of India"}))



# output ------------------------------------
'''
## India's Economic Landscape: A Mixed Bag of Growth and Challenges

**Introduction:** India, the world's seventh-largest economy, is navigating a complex economic landscape marked by both promising advancements and persistent hurdles. While recent years have seen remarkable growth and significant improvements, challenges such as inflation, unemployment, and economic inequality remain significant forces to contend with.

**Strengths:**

* **Strong GDP growth:** India has one of the fastest-growing economies in the world, averaging around 6% for the past few years. This is powered by factors like a young and rapidly expanding workforce, rising consumer spending, and significant investments in infrastructure and technology.
* **Innovation and digitalization:** India is a global frontrunner in digital innovation. The rise of e-commerce, fintech, and the booming IT sector, fueled by a strong internet penetration and increasing digital literacy, has contributed significantly to economic growth.
* **Emerging industrial sectors:** Manufacturing, particularly in the electronics and automotive sectors, is rapidly expanding, presenting immense growth opportunities for the Indian economy.
* **Government reforms:** The government has introduced various reforms, including the Goods and Services Tax (GST) and Make in India initiatives, aimed at streamlining regulations and creating a more favorable investment environment.

**Challenges:**

* **High inflation:** Persistent inflationary pressure has recently impacted everyday consumers. While this is a global phenomenon, higher-than-expected price increases on essential goods and services pose a challenge for economic stability and purchasing power.
* **Unemployment:** Despite significant job creation in certain sectors, unemployment remains a concern, particularly for young people. This highlights the need for job-driven growth and diversification beyond traditional industries.
* **Income inequality:** The gap between the rich and poor continues to widen in India, with access to opportunities, resources, and quality education remaining uneven across the population. This inequality impedes overall economic growth and development.
* **External factors:** Global economic instability, trade tensions, and rising commodity prices have posed potential risks to India's growth trajectory, affecting export-oriented industries and increasing their vulnerability.

**Outlook:**

While posed with these challenges, India approaches its future with great potential. Its demographics are favorable, its technological abilities are strong, and its government is striving to create an enabling environment for sustainable and inclusive growth.

It is crucial that India focuses on:

* **Maintaining sound fiscal and monetary policy** to manage inflation and prioritize inclusive growth.        
* **Reducing poverty and promoting social inclusion** through targeted programs and investments in education and healthcare.
* **Fostering a skilled and diverse workforce** to match the needs of emerging industries.
* **Investment in infrastructure development** and making progress on sustainable development goals.

**Conclusion:**

India's economic story isn't a chapter of one single occurrence, but a continuous unfolding process with ups and downs. By addressing its challenges head-on and leveraging its unique strengths, it has the potential to emerge stronger and more prosperous in the years to come.


**Disclaimer:** This report provides a brief overview of India's economic situation and aims to inform, not give investment advice.
'''