from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import JsonOutputParser

from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

parser = JsonOutputParser()
#1st prompt: Detailed report

template1 = PromptTemplate(
    template = 'give me the name, age, city of a fictional personal,\n {format_instruction}',
    input_variables = [],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
)
prompt = template1.format()

#chain = template1 | model | parser | template2 | model | parser  # chain usecase

result2 = model.invoke(prompt)

print(result2.content) 