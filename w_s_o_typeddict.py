from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

#schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)
result = structured_model.invoke("""Your seems working fine but i can see that there are couple issues noted with the performance of HDD." \
"which should be fixed inorder to get htings working well""")

print(result)

