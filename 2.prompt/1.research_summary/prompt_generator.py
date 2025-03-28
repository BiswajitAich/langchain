from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    input_variables=["paper_name", "style", "length"],
    template="""
You are an expert AI summarizer. Your task is to generate a summary of the research paper titled "{paper_name}".
Summarize the paper in a {length} explanation using a {style} approach.
Focus on the key contributions, methodologies, and findings of the paper.
Make sure to present the information in a clear, concise, and engaging manner appropriate for the chosen style.

""",
validate_template=True
)
template.save('./prompt/1.research_summary/template.json')