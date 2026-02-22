from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableSequence , RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

prompt1 = PromptTemplate(
    template= 'write joke about  {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()



prompt2 = PromptTemplate(
    template= 'explain the following joke  {text}',
    input_variables= ['text']
)

joke_gen_chain = RunnableSequence(prompt1, model , parser)

parallel_chain = RunnableParallel(
    {
    'word_count ' : RunnableLambda(lambda x : len(x.split())),
    'joke' : RunnablePassthrough()
    }
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic' : 'AI'})

print(result)