from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

load_dotenv()

model = ChatOpenAI()
prompt = PromptTemplate(
    template = 'write a summary for the following poem - \n {poem}',
    input_variables= ['poem']
)
parser = StrOutputParser()

loader = TextLoader('DocumentLodaders\\cricket.txt', encoding='utf-8')

docs = loader.load()

chain = prompt | model | parser

result  = chain.invoke({'poem' : docs[0].page_content})

print(docs)
print(type(docs))
print(len(docs))
print(type(docs[0].page_content))
print(docs[0].metadata)

print(result)