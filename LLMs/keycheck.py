from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("HUGGINGFACEHUB_ACESSS_TOKEN")

# Add this line to see the output
if api_key:
    print(f"API Key found: {api_key[:5]}...") # Prints only the first 5 chars for safety
else:
    print("API Key NOT found. Check your .env file.")