from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# Step1 a - Indexing (Document Ingestion)
try:
    video_id = "Gfr50f6ZBvo"

    # 1. Instantiate the class first (THIS IS THE MISSING LINE)
    ytt_api = YouTubeTranscriptApi()
    
    # 2. Call .fetch() on the instance, not the class
    transcript_list = ytt_api.fetch(video_id,languages=["en"])

    #flatten it to the text 
    transcript = " ".join(snippet.text for snippet in transcript_list)
    #print(transcript)
    #print(transcript_list.to_raw_data())

except TranscriptsDisabled:
    print("No caption Available for this video")


splitter  = RecursiveCharacterTextSplitter(
    chunk_size = 1000, 
    chunk_overlap = 200
)
chunks = splitter.create_documents([transcript])
#print(chunks[0])

embedding = OpenAIEmbeddings()

vector_store = FAISS.from_documents(chunks, embedding)

retriver = vector_store.as_retriever(search_type = "similarity", search_kwargs={"k":4})

result = retriver.invoke('what is deepmind?')
#print(result)
# 3 augmentation 
llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0.2)

prompt = PromptTemplate(
    template=""" you are helpfull assistant.
    Answer only from the provided trascript context.
    if context is insufficient, just say don't know.
    {context}
    Question:{question}
    """,
    input_variables=['context','question']
)
question = "is the topic of aliens discussed in this video? if yes then what is discussed"
retrived_docs = retriver.invoke(question)
def format_doc(retrived_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrived_docs)
    return context_text
# Parrallel chain
Parallel_chain = RunnableParallel({
    'context' : retriver | RunnableLambda(format_doc),
    'question': RunnablePassthrough()
}
)
parser = StrOutputParser()

main_chain = Parallel_chain | prompt | llm | parser

result = main_chain.invoke("can you summerize this video")

print(result)