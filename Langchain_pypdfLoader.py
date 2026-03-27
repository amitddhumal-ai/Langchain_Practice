from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Assignment_2_ML.pdf')

docs = loader.load()

print(docs)
