from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
import os
os.environ["USER_AGENT"] = "MyCoolScraper/1.0"
load_dotenv()
url = "https://en.wikipedia.org/wiki/List_of_Apple_products"
loader = WebBaseLoader(url)

docs = loader.load()

prompt = PromptTemplate(
    template= 'answer the following question \n {questions} from the following text {text}',
    input_variables=['questions','text']
)

parser = StrOutputParser()

model = ChatOpenAI()

chain = prompt | model | parser

print(docs[0].page_content)

result = chain.invoke({'questions':'what product appele release betwee 1990 and 2005?', 'text': docs[0].page_content})

print(result)