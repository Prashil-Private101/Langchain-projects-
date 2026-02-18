from pydantic import BaseModel , EmailStr, Field

from typing import Optional 

class Student(BaseModel):
    name : str
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt = 0, lt= 10, default = 0, description= 'a decimal number between 0 and 10')


new_student = {'name' : 'prashil', 'age': 30,'email':'prashil@abs.com','cgpa':9.5}

student = Student(**new_student)

print(type(student))
print(student.name)
print(student.age)

dict_student = dict(student)

student_json = student.model_dump_json()
print(type(dict_student))
print(type(student_json))