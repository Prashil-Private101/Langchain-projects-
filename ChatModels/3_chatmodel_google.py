from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model= 'gemini-2.5-flash',temperature = 1.7)

result= model.invoke("Whait is the capital of India?")

print(result)

print("\n", result.text)

