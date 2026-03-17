from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document
load_dotenv()

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

embedding_model = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(
    documents= docs,
    embedding=embedding_model
)

retriver = vectorstore.as_retriever(
    search_type= "mmr",
    search_kwargs = {"k":3, "lambda_mult":0.5}

)

query = "what is langchin?"
result  = retriver.invoke(query)

for i , doc in enumerate(result):
    print(f"\n-----Result{i+1}-----")
    print(doc.page_content)