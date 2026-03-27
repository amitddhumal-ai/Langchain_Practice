from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("air-pollution.txt", encoding='utf-8')
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=100)
chunks = splitter.split_documents(docs)

print(type(docs))  
#print(docs[0])
#print(docs[0].page_content)
#print(docs[0].metadata)

print(chunks[0].page_content)