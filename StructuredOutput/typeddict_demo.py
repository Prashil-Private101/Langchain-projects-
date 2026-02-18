from typing import TypedDict

class Person(TypedDict):
    name : str 
    age : int


new_Person : Person = {'name' : 'prashil' , 'age' : 30}

print(new_Person)