from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import json

load_dotenv()

with open('json_schema.json', 'r') as file:
    review_schema = json.load(file)

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
structured_model = model.with_structured_output(review_schema)
result = structured_model.invoke(
    """
    I recently bought the XYZ Smartwatch, and overall, I am quite happy with my purchase. 
    The battery life is impressive, lasting almost a week on a single charge. 
    The fitness tracking features are accurate, and the display is bright and easy to read even in sunlight. 
    However, I found the app interface a bit cluttered, and the watch lacks third-party app support. 
    Despite these minor drawbacks, it's a great value for the price.
    """
)

print(result)
print("\n\n")
print("summary == ", result[0]['args'].get('summary', []))
print("\n\n")
print("sentiment == ", result[0]['args'].get('sentiment', []))
print("\n\n")
print("pros == ", result[0]['args'].get('pros', []))
print("\n\n")
print("cons == ", result[0]['args'].get('cons', []))
print("\n\n")