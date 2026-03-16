from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash',temperature=0.2)
result = model.invoke("Give me 5 random Indian names:")

print(result.content)