from langchain.tools import BaseTool
from typing import Type 
from pydantic import BaseModel , Field

class MultiplyInput(BaseModel):
    a: int = Field(required = True, description="the first number to add")
    b: int = Field(required=True, description="the second number to add")

class MultiplyTool(BaseTool):
    name: str = "nultiply"
    description : str = "multiply two integers"
    args_schema: type[BaseModel] = MultiplyInput

    def _run(self, a: int , b:int) ->int:
        return a*b

multiply_tool = MultiplyTool() 
result = multiply_tool.invoke({"a":3,"b":5})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)

print(multiply_tool.args_schema.model_json_schema())