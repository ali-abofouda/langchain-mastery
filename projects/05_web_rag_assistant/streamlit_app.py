import os
import streamlit as st
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

# 1. إعدادات الصفحة والـ Theme (Dark Mode)
st.set_page_config(
    page_title="Web RAG Assistant 🌐",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تحميل متغيرات البيئة
load_dotenv(find_dotenv())

# 3. تصميم الـ CSS الخاص بالـ Dark Mode المحسّن
st.markdown("""
<style>
    /* الإعدادات العامة للمظهر الداكن */
    .stApp {
        background-color: #0E1117;
        color: #E0E0E0;
    }

    /* الشريط الجانبي */
    section[data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #30363D;
    }

    /* العناوين والبطاقات */
    .main-header {
        background: linear-gradient(90deg, #1F6FEB 0%, #238636 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.3rem;
        margin-bottom: 0.5rem;
    }

    .sub-header {
        color: #8B949E;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }

    /* صندوق الرسائل والمحادثة */
    .stChatMessage {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 0.8rem;
    }

    /* الأزرار وحقول المدخلات */
    .stButton>button {
        background-color: #238636;
        color: #FFFFFF;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #2EA043;
        box-shadow: 0px 4px 12px rgba(46, 160, 67, 0.3);
    }

    /* شارات الميتاداتا */
    .stat-badge {
        background-color: #21262D;
        border: 1px solid #30363D;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        text-align: center;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)


def format_docs(docs):
    return "\n\n---\n\n".join(doc.page_content for doc in docs)


@st.cache_resource(show_spinner=False)
def load_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def process_url(url: str):
    """تحميل المقال وتقطيعه وتخزينه في قاعدة بيانات Chroma."""
    try:
        with st.spinner("🌐 جاري سحب وتنزيل محتوى المقال من الويب..."):
            loader = WebBaseLoader(url)
            raw_docs = loader.load()

        if not raw_docs:
            st.error("❌ لم يتم العثور على محتوى في الرابط المرفق.")
            return None, 0

        with st.spinner("✂️ جاري تقطيع النص وإعداد التضمينات المتجهة..."):
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = splitter.split_documents(raw_docs)

            embeddings = load_embeddings()
            vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
            retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        return retriever, len(chunks)
    except Exception as e:
        st.error(f"⚠️ حدث خطأ أثناء المعالجة: {e}")
        return None, 0


def get_rag_chain(retriever):
    """بناء سلسلة الـ RAG عبر LCEL مع Groq."""
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "أنت مساعد ذكي متخصص في استخراج المعلومات الموثوقة من المقالات التقنية وأوراق الأبحاث.\n"
                   "استخدم السياق المرفق فقط للإجابة على سؤال المستخدم بشكل مفصل ودقيق.\n"
                   "إذا كانت المعلومة غير متوفرة في السياق، أجب بصراحة: 'المعلومة المطلوبة غير مذكورة في هذا المقال'.\n\n"
                   "السياق المتاح:\n{context}"),
        ("human", "{question}")
    ])

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain


# --- الواجهة الرئيسية ---
st.markdown('<div class="main-header">🌐 Web RAG Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">مساعد ذكي للدردشة والاستعلام المباشر من المقالات وأوراق الأبحاث عبر الويب</div>', unsafe_allow_html=True)

# الشريط الجانبي (Sidebar)
with st.sidebar:
    st.header("⚙️ إعدادات المقال")
    default_url = "https://lilianweng.github.io/posts/2023-06-23-agent/"
    target_url = st.text_input("رابط مقال الويب:", value=default_url, help="أدخل أي رابط لصفحة ويب أو مقال للتحدث معه")

    process_btn = st.button("🚀 معالجة وفهرسة المقال", use_container_width=True)

    st.markdown("---")
    st.markdown("### 📊 حالة النظام")
    if "chunks_count" in st.session_state:
        st.markdown(f"""
        <div class="stat-badge">
            ✅ <b>المقال مفهرس بنجاح</b><br>
            📦 عدد القطع النصية: <b>{st.session_state.chunks_count}</b>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("💡 اضغط على زر المعالجة لبدء الفهرسة.")

    st.markdown("---")
    if st.button("🗑️ مسح المحادثة", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# معالجة الرابط عند الضغط
if process_btn or "retriever" not in st.session_state:
    if target_url:
        retriever, count = process_url(target_url)
        if retriever:
            st.session_state.retriever = retriever
            st.session_state.chunks_count = count
            st.session_state.rag_chain = get_rag_chain(retriever)
            st.session_state.messages = []
            st.success("✅ تم بناء قاعدة المتجهات وتجهيز المساعد التفاعلي!")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# إدخال سؤال جديد
if user_query := st.chat_input("اطرح سؤالك حول المقال المفهرس..."):
    # إضافة سؤال المستخدم
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)

    # التوليد والاستجابة
    if "rag_chain" in st.session_state:
        with st.chat_message("assistant"):
            with st.spinner("🤖 جاري البحث في المقال وتوليد الإجابة..."):
                answer = st.session_state.rag_chain.invoke(user_query)
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
    else:
        st.error("⚠️ يرجى معالجة رابط المقال أولاً من الشريط الجانبي.")
