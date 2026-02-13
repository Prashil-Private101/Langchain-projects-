from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model= "claude-3.5-sonnet-20241022")

results = model.invoke('What is the capital of Inida?')

print(results)