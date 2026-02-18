from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

from typing import TypedDict 

load_dotenv()

model = ChatOpenAI(model= 'gpt-4o-mini')

# Schema for the structured output 

class Review(TypedDict):
    
    summery : str
    sentiment : str

Structured_model = model.with_structured_output(Review)

result = Structured_model.invoke(
    """ the hardware is great, but the software feels boated. there are too many preinstalled apps
             that I can't remove. Also the UI looks outdated compare to other brands. Hoping for a sottware update to fix this.
             """
             )

print(result)
print(result['summery'])
print(result['sentiment'])

