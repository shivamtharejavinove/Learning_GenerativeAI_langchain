from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import json

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

review_text = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! ...
Review by Nitish Singh
"""

prompt = f"""Analyze the following product review and return ONLY a valid JSON object — no extra text, no markdown code fences.

The JSON must have exactly these keys:
- key_themes: a list of strings
- summary: a string
- sentiment: either "pos" or "neg"
- pros: a list of strings, or null
- cons: a list of strings, or null
- name: a string, or null

Review:
{review_text}
"""

response = model.invoke(prompt)

raw_output = response.content.strip()
if raw_output.startswith("```"):
    raw_output = raw_output.strip("`").replace("json", "", 1).strip()

result = json.loads(raw_output)
print(result)
print(result["summary"])
print(result["sentiment"])