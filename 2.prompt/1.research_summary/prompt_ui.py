import streamlit as st
from langchain_core.prompts import load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm_model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

st.header("Research Tool")

paper_input = st.selectbox(
    "Select research paper Name",
    [
        "Attention Is All You Need (2017)",
        "Generative Adversarial Networks (2014)",
        "ImageNet Classification with Deep Convolutional Neural Networks (AlexNet, 2012)",
        "Deep Residual Learning for Image Recognition (ResNet, 2015)",
        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2018)",
        "Playing Atari with Deep Reinforcement Learning (2013)",
        "AlphaGo Zero: Mastering the Game of Go Without Human Knowledge (2017)",
        "GPT-3: Language Models are Few-Shot Learners (2020)",
        "CLIP: Connecting Text and Images (2021)",
        "DALL-E: Zero-Shot Text-to-Image Generation (2021)",
    ],
)
style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-friendly",
        "Academic and Formal Style",
        "Journalistic Style",
        "Conversational/Explanatory Style",
        "Narrative Storytelling Style",
    ],
)
length_input = st.selectbox(
    "Select Explanation length",
    ["Short (1-2 paragraph)", "Medium (3-5 paragraph)", "Long (detailed explanation)"],
)

template = load_prompt('./prompt/1.research_summary/template.json')

if st.button("Summarize"):
    chain = template | llm_model
    result = chain.invoke(
        {"paper_name": paper_input, "style": style_input, "length": length_input}
    )
    st.subheader("Template Text")
    st.write(template.template)

    st.subheader("Summary")
    st.write(result.content)