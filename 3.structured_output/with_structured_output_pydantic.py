from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal

load_dotenv()

class Review(BaseModel):
    summary: list[str] = Field(description="A one line summary of the review.")
    sentiment: Literal['pro', 'con', 'neu'] = Field(description="Return sentiment as Positive, negative or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write all the cons inside a list")
    name: Optional[str] = Field(default='NO_NAME', description="Write the name of the reviewer")

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
structured_model = model.with_structured_output(Review)
result = structured_model.invoke(
    """
    I recently bought the XYZ Smartwatch, and overall, I am quite happy with my purchase. 
    The battery life is impressive, lasting almost a week on a single charge. 
    The fitness tracking features are accurate, and the display is bright and easy to read even in sunlight. 
    However, I found the app interface a bit cluttered, and the watch lacks third-party app support. 
    Despite these minor drawbacks, it's a great value for the price.
    """
)
print(result, sep='\n\n')
print(result.summary, sep='\n\n')
print(result.sentiment, sep='\n\n')
print(result.pros, sep='\n\n')
print(result.cons, sep='\n\n')
print(result.name, sep='\n\n')