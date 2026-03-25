from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

class Person(BaseModel):
    name: str = Field(description='Person name')
    age: int = Field(description='Persons age')
    city: str = Field(description='Persons city')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'give me the name, age, city of a fictional {place} person,\n {format_instruction}',
    input_variables = ['place'],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
)
prompt = template.invoke({'place':'indian'})

#chain = template1 | model | parser  # chain usecase

print(prompt)  # helps undrstand what prompt is feeded to llm

result2 = model.invoke(prompt)

print(result2.content) 