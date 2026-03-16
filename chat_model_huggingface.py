
## Not Working

'''
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="microsoft/DialoGPT-large", task = "text-generation",max_new_tokens=256)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital on Israel")
print(result)

'''

from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="gpt2",                    
    task="text-generation",
    max_new_tokens=100,
    temperature=0.7
)

result = llm.invoke("What is the capital of Israel? Answer:")
print(result)

