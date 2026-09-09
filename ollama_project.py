import os

import streamlit as st
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# =========================
# Environment
# =========================

load_dotenv()

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY", "")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT", "")
os.environ["LANGSMITH_TRACING"] = "true"


# =========================
# Prompt
# =========================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. "
            "Answer the question as truthfully as possible, "
            "and if you don't know the answer, say 'I don't know.'"
        ),
        ("user", "Question: {input}")
    ]
)


# =========================
# Model
# =========================

llm = OllamaLLM(
    model="qwen3:8b"
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser


# =========================
# Streamlit
# =========================

st.title("Ollama + LangSmith Example using Qwen3 8B")

input_text = st.text_input("Enter your question here:")

if input_text:
    response = chain.invoke(
        {"input": input_text}
    )

    st.write(response)