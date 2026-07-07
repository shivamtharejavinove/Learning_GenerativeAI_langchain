from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)  # dimension of the vector 

embedding.embed_query("delhi is the capital of India")

result = embedding.embed_query("delhi is the capital of India")
print(str(result))

