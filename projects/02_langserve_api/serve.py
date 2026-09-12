import os
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

load_dotenv(find_dotenv())

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    max_tokens=1000,
)

system_template = "You are a helpful assistant. Answer the question as truthfully as possible, and if you don't know the answer, say 'I don't know.'"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "Question: {input}"),
])

parser = StrOutputParser()
chain = prompt_template | model | parser

app = FastAPI(
    title="LangChain + Groq API Server",
    version="1.0.0",
    description="This is a simple example of using LangChain with Groq to answer questions exposed via FastAPI & LangServe."
)

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
