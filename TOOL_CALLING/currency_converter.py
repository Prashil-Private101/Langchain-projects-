from langchain_core.tools import tool, InjectedToolArg
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv, get_key
from typing import Annotated
import json
load_dotenv()

api_key = get_key('.env','YOUR-API-KEY')


@tool
def get_conversion_factor(base_currency:str , targetc_currancy:str) ->float:
    '''this function fetches the conversion factor'''
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{targetc_currancy}"

    response = requests.get(url)
    return response.json()


@tool
def convert(base_currency_value: float, conversion_rate: Annotated[float, InjectedToolArg]) ->float:
    '''given currency conversion rate this fuction calculates target currency value from given base currency value'''
    return base_currency_value * conversion_rate



class CurrencyConver:
    def get_tools(self):
        return [ get_conversion_factor,convert]
    
toolkit = CurrencyConver()
tools = toolkit.get_tools()
get_conversion_factor.invoke({'base_currency':'USD', 'targetc_currancy':'INR'})
convert.invoke({'base_currency_value':10.0, 'conversion_rate':85.5})
# tool bindind
llm = ChatOpenAI()
llm_with_tool = llm.bind_tools(tools)

query = HumanMessage('what is the conversion factor between USD and INR, and based on that can you convert 100 USD to INR')
messages = [query]
ai_message = llm_with_tool.invoke(messages)
messages.append(ai_message)


for tool_call in ai_message.tool_calls:
    # execute the fist tool and get value of conversion rate 
    if tool_call['name'] == 'get_conversion_factor':
        tool_message1 = get_conversion_factor.invoke(tool_call)
        messages.append(tool_message1)
        conversion_rate = json.loads(tool_message1.content)['conversion_rate']

    if tool_call['name'] == 'convert':
        tool_call['args'] ['conversion_rate'] = conversion_rate
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)

result = llm_with_tool.invoke(messages)
print(result.content)