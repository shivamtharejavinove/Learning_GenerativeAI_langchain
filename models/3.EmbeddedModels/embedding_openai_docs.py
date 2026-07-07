from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)  # dimension of the vector 

documents = [
    "delhi is the capital of India",        
    " paris is the capital of France", 
    "london is the capital of UK",
]

result = embedding.embed_documents(documents)

print(str(result))

