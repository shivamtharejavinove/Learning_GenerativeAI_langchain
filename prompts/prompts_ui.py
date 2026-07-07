from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

st.header('research tool')

paper_input = st.selectbox("Select research paper name",["Select...", "Attention is all you need", "BERT: Pre-training of deep bidirectional transformers", "Language Models are Few-Shot Learners", "Diffusion models beat GANs on Image synthesis"])

style_input = st.selectbox("Select Explanation style",["Beginner-friendly", "Technical", "Code-oriented", "Mathematical"])

length_input = st.selectbox("Select the length style",    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed)"])

user_input = st.text_input('Enter your prompt')


template = load_prompt('template.json')

# prompt =template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'length_input' : length_input,
# })
# if st.button('summarize'):
#     # st.text('somerandom text')
#     result = model.invoke(prompt)
#     st.write(result.content)


#  now as we are calling invoke function twice, once for model and other time for template function instead we chain them together with chain function through which we can call invoke once for both 

if st.button('summarize'):
    chain = template | model 
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input' : length_input,
    })
    st.write(result.content)