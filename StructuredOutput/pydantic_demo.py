from pydantic import BaseModel

from typing import Optional 

class Student(BaseModel):
    name : str
    age : Optional[int] = None


new_student = {'name' : 'prashil', 'age': 30}

student = Student(**new_student)

print(type(student))
print(student.name)
print(student.age)