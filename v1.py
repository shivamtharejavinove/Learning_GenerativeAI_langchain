# dynamic and reusable prompts

# from langchain_core.prompts import PromptTemplate      
#                     
# prompt =  PromptTemplate.from_template('summarize {topic} in {emotion} tone')         # version 1
# print(prompt.format(topic='cricket', emotion='excited'))

# from langchain_core.prompts import PromptTemplate                       verison 2
# prompt = PromptTemplate(
#     template='summarize {topic} in {emotion} tone',
#     input_variables=['topic', 'emotion']
# )
# print(prompt.format( topic='cricket', emotion='excited'))



# role-based prompts
# from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
# chat_prompt = ChatPromptTemplate.from_messages([
#     ("system", "hi, you are a experienced {profession} "),
#     ("user", "Tell me about {topic}")
# ])
# formatted_messages = chat_prompt.format_messages(profession='doctor', topic='heart disease')
# print(formatted_messages)


# from now the code will be on models // langchain-> models 
# /home/shivam/Documents/genAI/.venv/bin/python -m pip install langchain langchain-core
# pip install langchain langchain-core

import langchain

print(langchain.__version__)


