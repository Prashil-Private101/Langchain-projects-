from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import JsonOutputParser

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b:fastest",
    task="text-generation",
    #max_new_tokens=100,
   # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()


template = PromptTemplate(template= ' give me the name age and city of the fictional person \n {format_instruction}',
               input_variables = [],
               partial_variables={'format_instruction':parser.get_format_instructions()}
               )

prompt = template.format()

print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content)


print(final_result)

print(type(final_result))