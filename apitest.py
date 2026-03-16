import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = "AIzaSyCJtS-1MBEB_wxTZaF_QH5_Wo0sZmsAZ44"

# ✅ EXACT FROM YOUR LIST
llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")
print("✅ Gemini LOADED!")

response = llm.invoke("Hi Amit! LangChain + Gemini working perfectly?")
print("✅ SUCCESS:", response.content)
