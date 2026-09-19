import os
import sys
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# تحميل متغيرات البيئة
load_dotenv(find_dotenv())


def format_docs(docs):
    """تجميع وتنسيق المستندات المسترجعة في نص واحد للسياق."""
    return "\n\n---\n\n".join(doc.page_content for doc in docs)


def build_rag_chain(url: str):
    """سحب المقال من الإنترنت وبناء سلسلة الـ RAG كاملة."""
    print(f"\n🌐 [1/4] جاري تحميل محتوى المقال من: {url}")
    loader = WebBaseLoader(url)
    docs = loader.load()

    if not docs:
        raise ValueError("❌ تعذر تحميل المحتوى من الرابط المرفق.")

    print(f"✅ تم تحميل المستند ({len(docs[0].page_content)} حرفاً).")

    print("✂️ [2/4] جاري تقسيم النص إلى قطع دلالية (Chunking)...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ". ", " "]
    )
    chunks = text_splitter.split_documents(docs)
    print(f"✅ تم استخراج {len(chunks)} قطعة نصية.")

    print("⚡ [3/4] جاري إنشاء التضمينات وبناء قاعدة بيانات المتجهات Chroma DB...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    print("🤖 [4/4] تهيئة نموذج التوليد Groq وسلسلة الـ LCEL...")
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "أنت مساعد ذكي متخصص في تحليل واستخراج المعلومات من مقالات الويب الأكاديمية والتقنية.\n"
                   "أجب على سؤال المستخدم بدقة ومباشرة بالاعتماد على السياق المرفق فقط.\n"
                   "إذا لم تكن المعلومة موجودة في السياق، اذكر بصراحة أنك لا تملك المعلومة بناءً على المقال.\n\n"
                   "السياق:\n{context}"),
        ("human", "{question}")
    ])

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    print("✅ تم إعداد مساعد RAG بنجاح!\n")
    return rag_chain


def main():
    print("=" * 65)
    print("🌐 Web RAG Assistant - تطبيق استعلام المقالات بـ LangChain & Groq")
    print("=" * 65)

    default_url = "https://lilianweng.github.io/posts/2023-06-23-agent/"
    user_url = input(f"أدخل رابط المقال (اضغط Enter للاستخدام الافتراضي):\n[{default_url}]: ").strip()
    target_url = user_url if user_url else default_url

    try:
        rag_chain = build_rag_chain(target_url)
    except Exception as e:
        print(f"❌ حدث خطأ أثناء إعداد السلسلة: {e}")
        sys.exit(1)

    print("💬 يمكنك الآن طرح أسئلتك حول المقال (اكتب 'exit' للخروج):")
    print("-" * 65)

    while True:
        try:
            query = input("\n❓ سؤالك: ").strip()
            if not query:
                continue
            if query.lower() in ["exit", "quit", "خروج"]:
                print("👋 شكراً لاستخدامك مساعد الـ Web RAG!")
                break

            print("\n🤖 جاري التفكير واسترجاع الإجابة...")
            response = rag_chain.invoke(query)
            print("\n💬 الإجابة:")
            print(response)
            print("-" * 65)
        except KeyboardInterrupt:
            print("\n👋 تم إغلاق البرنامج.")
            break
        except Exception as e:
            print(f"⚠️ حدث خطأ أثناء تنفيذ الاستعلام: {e}")


if __name__ == "__main__":
    main()
