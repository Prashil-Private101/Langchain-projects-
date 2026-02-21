from langchain_openai import ChatOpenAI 
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_classic.schema.runnable import RunnableParallel, RunnableBranch,  RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser0 = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive' , 'negetive'] = Field(description='give the sentiment of the feedack')

parser1 = PydanticOutputParser(pydantic_object= Feedback)
prompt1 = PromptTemplate(
    template='Classify the Sentiment of the following feedback text into positive or negetive \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction' : parser1.get_format_instructions()}

)

classifier_chain = prompt1 | model | parser1


#result = classifier_chain.invoke({'feedback' : 'This is a terrible smartphone'}).sentiment

prompt2 = PromptTemplate(
    template= 'Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template= 'Write an appropriate response to this negetive feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2| model | parser0),
    (lambda x:x.sentiment == 'negetive', prompt3| model | parser0),
    RunnableLambda(lambda x:"could not find sentiment ")
)

chain = classifier_chain | branch_chain

result = (chain.invoke({'feedback' : 'this is a terrible terrible smartphone'}))

print(result )