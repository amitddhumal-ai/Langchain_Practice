from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} assistant'),
    ('human', 'Tell me about {topic}')
])

prompt = chat_template.invoke({'domain':'football','topic':'players'})

print(prompt)