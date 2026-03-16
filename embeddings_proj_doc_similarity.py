from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embedding = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001")

documents = [
    "Sachin Tendulkar scored 100 international centuries, revolutionizing Indian cricket with his masterful technique and unbreakable concentration across formats.",
    "Virat Kohli transformed Indian batting aggression, leading with 80 centuries and multiple ICC trophies while dominating as captain across all formats.",
    "Kapil Dev captained India to the historic 1983 World Cup triumph, taking 434 Test wickets and revolutionizing all-round cricket with his swing bowling.",
    "MS Dhoni masterminded three ICC trophies including 2011 World Cup, revolutionizing wicketkeeping with helicopter shots and calm leadership under pressure.",
    "Rahul Dravid anchored India's Test batting with 13,288 runs, mentoring young talents while achieving overseas victories as 'The Wall' of defense"]

query = "Tell me about Sachin Tendulkar"

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embedding)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is: ",score)