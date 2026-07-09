from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm1)

prompt = PromptTemplate(
    template = 'write a summary for the following poem - \n {poem}',
    input_variables= ['poem']
)

parser = StrOutputParser()
loader = TextLoader('cricket.txt',encoding = 'utf-8')

docs = loader.load()

print(type(docs))
print(type(docs))
print(len(docs))          # how many documents were loaded (usually 1 for a single text file)
print(docs[0].page_content)   # the actual text content
print(docs[0].metadata)        # info like source filename
chain = prompt | model | parser 
print(chain.invoke({'poem':docs[0].page_content}))