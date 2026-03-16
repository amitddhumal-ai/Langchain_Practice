from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    "Delhi is capital of India",
    "Paris is capital of France",
    "Tel Aviv is capital of Israel"
]

embedding = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001")
result = embedding.embed_documents (documents)

print(str(result))