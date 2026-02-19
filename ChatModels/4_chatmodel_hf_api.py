import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

# 1. Setup the underlying LLM via Endpoint
# 'google/gemma-2-2b-it' often requires a dedicated endpoint; 
# Zephyr is a better 'all-rounder' for the free serverless API.
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b:fastest",
    task="text-generation",
    max_new_tokens=100,
   # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

# 2. Wrap it in ChatHuggingFace to handle chat templates (special tokens like <|user|>)
model = ChatHuggingFace(llm=llm)

# 3. Define your messages
messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="What is the capital of India?")
]

# 4. Invoke the model
response = model.invoke(messages)

print(response.content)