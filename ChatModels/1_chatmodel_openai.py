from langchain_openai import ChatOpenAI

from dotenv import load_dotenv 

load_dotenv()

model = ChatOpenAI(model='gpt-4',temperature=1.3 ,max_completion_tokens= 10 ) # change Temperature value to higher side 
# restrict completion token 

result = model.invoke("write a 5 line poem on cricket")

print(result)

print(result.content)