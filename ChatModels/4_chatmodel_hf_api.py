from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Nanbeige/Nanbeige4.1-3B", 
    task= "text-generation"
    )
model = ChatHuggingFace(llm = llm )

result = model.invoke("what is the capital of india")

print(result)