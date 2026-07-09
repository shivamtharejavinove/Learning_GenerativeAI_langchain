from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm1)


prompt1  = PromptTemplate(
    template= 'write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template= 'explain the following joke {text}',
    input_variables=['text']
)



chain  = RunnableSequence(prompt1, model, parser, prompt2, model,parser)

print(chain.invoke({'topic':'AI'}))
