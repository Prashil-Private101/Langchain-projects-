from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

ChatPromptTemplate([
    ('system', ' You are a helpful customer support agent '),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_hisory = []

# load chat history 
with open('Prompts/chat_history.txt') as f:
    chat_hisory.extend(f.readlines())


print(chat_hisory)

#create prompt

chat_tem