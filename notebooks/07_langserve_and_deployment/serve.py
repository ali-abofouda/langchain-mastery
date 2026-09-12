import os
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

# تحميل المفاتيح ومتغيرات البيئة
load_dotenv(find_dotenv())

if not os.getenv("GROQ_API_KEY"):
    print("⚠️ تحذير: لم يتم العثور على GROQ_API_KEY في البيئة.")

# تهيئة نموذج المحادثة
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    max_tokens=1000,
)

# إنشاء قالب التوجيه
system_template = "You are a helpful assistant. Answer the question as truthfully as possible, and if you don't know the answer, say 'I don't know.'"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "Question: {input}"),
])

parser = StrOutputParser()

# بناء سلسلة LCEL
chain = prompt_template | model | parser

# إنشاء تطبيق FastAPI
app = FastAPI(
    title="LangChain + Groq API Server",
    version="1.0.0",
    description="خادم REST API مبني باستخدام FastAPI و LangServe لتوفير إجابات موثقة عبر نماذج Groq السريعة."
)

# إضافة مسارات LangServe للتطبيق
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    print("🚀 جاري تشغيل خادم LangServe على http://localhost:8000 ...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
