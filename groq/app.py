from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st
import os
from dotenv import load_dotenv

groq_api_key=os.getenv("GROQ_API_KEY")

## Prompt Template
    
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With Chat Groq')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="mixtral-8x7b-32768")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
    