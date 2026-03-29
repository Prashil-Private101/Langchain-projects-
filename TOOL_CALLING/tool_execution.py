from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv
load_dotenv()



@tool
def add(a: int , b: int ) -> int:
    """add two numbers"""
    return a+b

@tool
def multiply(a: int , b: int)-> int:
    """ multiply two numbers"""
    return a*b

class MathToolkit:
    def get_tools(self):
        return [add, multiply]
    
toolkit = MathToolkit()
tools = toolkit.get_tools()


for tool in tools:
    print(tool.name , "=>", tool.description)

muptiply_tool = tools[1]
result = muptiply_tool.invoke({'a':3 , 'b':5})
print(result)

llm = ChatOpenAI()
llm_with_tool = llm.bind_tools(tools)
query = HumanMessage('can you multiply 3 with 10')
messages =[ query ]
res = llm_with_tool.invoke(messages)
messages.append(res)
print(res.tool_calls[0])

tool_result = multiply.invoke(res.tool_calls[0])
messages.append(tool_result)
print(llm_with_tool.invoke(messages).content)