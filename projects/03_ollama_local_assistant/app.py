import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(find_dotenv())

os.environ["LANGSMITH_TRACING"] = "true"
if os.getenv("LANGSMITH_API_KEY"):
    os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. "
        "Answer the question as truthfully as possible, "
        "and if you don't know the answer, say 'I don't know.'"
    ),
    ("user", "Question: {input}")
])

llm = OllamaLLM(model="qwen3:8b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

st.title("🦙 Ollama Local Assistant + LangSmith")

input_text = st.text_input("Enter your question here:")

if input_text:
    with st.spinner("Thinking locally..."):
        try:
            response = chain.invoke({"input": input_text})
            st.write(response)
        except Exception as error:
            st.error(f"Failed to connect to local Ollama server: {error}")
