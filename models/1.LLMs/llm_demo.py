from langchain_openai import OpenAI
from dotenv import load_dotenv     # used to load an env variable which are stored in .env files 

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')   #creating an object OpenAI and putting it in variable llm and inside we are defining the gpt model which we will be using

result = llm.invoke("What is the capital of India?")   # using the invoke method to get the answer of the question

print(result)   # printing the result
