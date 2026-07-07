from langchain_openai import chatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = chatOpenAI(model='gpt-4', temperature=0.5, max_completion_tokens=1024) # you also add patamenters while specuifying model type  temperatures controls the randomness of the output, with higher values (e.g., 0.8) producing more random outputs and lower values (e.g., 0.2) producing more focused and deterministic outputs.  

result = model.invoke("what is the capital of India ?")

print (result.content)
# chat models give you something more than what llm give you as an answer because it is more advanced than llm and it is more capable of understanding the context of the question and
#  it can give you a more accurate answer than llm, like in an llm it gives ou just an answer but here you will get the answer but also will specify things like completion tokens, prompt tokens , 
# total tokens , additional_kwargs(key word arguments) and all other types of tokens which are used in the process of generating the answer and also it will give you the model name which is used to generate the answer and also it will give you the time taken to generate the answer and also it will give you the status of the answer whether it is successful or not and also it will give you the error message if there is any error in generating the answer and also it will give you the usage of the model which is used to generate the answer and also it will give you the cost of the model which is used to generate the answer and also it will give you the number of requests made to the model which is used to generate the answer and also it will give you the number of requests remaining for the model which is used to generate the answer and also it will give you the number of requests per minute for the model which is used to generate the answer and also it will give you the number of requests per day for the model which is used to generate the answer and also it will give you the number of requests per month for the model which is used to generate the answer and also it will give you the number of requests per year for the model which is used to generate the answer and also it will give you the number of requests per lifetime for the model which is used to generate the answer and also it will give you the number of requests per user for the model which is used to generate the answer and also it will give you the number of requests per organization for the model which is used to generate the answer and also it will give you the number of requests per

# just to get an answer you fetch the content from the result object(result.content)
