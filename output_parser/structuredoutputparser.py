# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen2.5-7B-Instruct",
#     task="text-generation",
# )

# model = ChatHuggingFace(llm=llm)

# schema = [
#     ResponseSchema(name='fact1', description='Fact1 about the topic'),
#     ResponseSchema(name='fact2', description='Fact2 about the topic'),
#     ResponseSchema(name='fact3', description='Fact3 about the topic')
# ]

# parser = StructuredOutputParser.from_response_schemas(schema)

# template = PromptTemplate(
#     template='Give 3 facts about {topic}\n{format_instruction}',
#     input_variables=['topic'],
#     partial_variables={'format_instruction': parser.get_format_instructions()}
# )

# prompt = template.invoke({'topic': 'black hole'})
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)







from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

class Facts(BaseModel):
    fact1: str = Field(description="Fact1 about the topic")
    fact2: str = Field(description="Fact2 about the topic")
    fact3: str = Field(description="Fact3 about the topic")

parser = PydanticOutputParser(pydantic_object=Facts)

template = PromptTemplate(
    template='Give 3 facts about {topic}\n{format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)


# prompt = template.invoke({'topic': 'black hole'})
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)