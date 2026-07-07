from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 150}
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text.\n{text}',
    input_variables=['text']
)

# Step 1: generate the report
prompt1 = template1.invoke({'topic': 'black hole'})
result = model.invoke(prompt1)

# Step 2: summarize the report we just got
prompt2 = template2.invoke({'text': result.content})
summary = model.invoke(prompt2)

print("Generating... please wait")
result = model.invoke(prompt1)
print("Done!")
print(result.content)


print("Full report:\n", result.content)
print("\nSummary:\n", summary.content)

