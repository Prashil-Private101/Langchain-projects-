from langchain_core.tools import tool

# final step 
@tool 
def multiply(a: int , b: int) -> int :
    """Multiply two integers"""
    return a*b

result = multiply.invoke({"a":3,"b":5})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)

print(multiply.args_schema.model_json_schema())