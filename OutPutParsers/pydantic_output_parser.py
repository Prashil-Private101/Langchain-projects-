from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate  

from langchain_classic.output_parsers import ResponseSchema,StructuredOutputParser, PydanticOutputParser

from pydantic import BaseModel, Field



load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    #max_new_tokens=100,
   # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name : str = Field(description='Name of the Person')
    age : int = Field(description='Age of the person')
    city : str = Field(description='name of the city of the person belong to')



parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
)

chain = template | model | parser

final_result = chain.invoke({'place' : 'indian'})

print(final_result)