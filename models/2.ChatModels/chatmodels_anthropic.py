# from langchain_anthropic import chatAnthropic
# from dotenv import load_dotenv
# load_dotenv()
# model = chatAnthropic(model='claude-3-5-sonnet-20241022')\
# result = model.invoke("who is the prime minister of India")\
# print(result.content)


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model='chat-bison-001', temperature=0.5, max_completion_tokens=1024) # you also add patamenters while specuifying model type  temperatures controls the randomness of the output, with higher values (e.g., 0.8) producing more random outputs and lower values (e.g., 0.2) producing more focused and deterministic outputs.
result = model.invoke("what is the capital of Indi  ```         a ?")

print (result.content)
