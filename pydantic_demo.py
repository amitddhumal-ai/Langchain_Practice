from pydantic import BaseModel

class Student(BaseModel):
    name: str

new_student = {'name':'amit'}
old_student = {'name':33}

student = Student(**new_student)
teacher = Student(**old_student)

print(student)
print(type(student))

print(teacher) # this does validation by showing an error. since name = str and value passed is int(33) 