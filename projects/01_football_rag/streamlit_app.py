import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

SOURCE_URL = "https://en.wikipedia.org/wiki/Association_football"


@st.cache_resource(show_spinner=False)
def build_rag_components():
    load_dotenv(find_dotenv())
    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError("GROQ_API_KEY is not set in the environment or .env file.")

    documents = WebBaseLoader(SOURCE_URL).load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
    vector_store = FAISS.from_documents(chunks, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.2,
        max_tokens=800,
    )
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a precise football knowledge assistant. Answer in the same language "
            "as the user's question. Use the provided context and give a useful explanation. "
            "If the context does not contain the answer, say the source does not cover it "
            "and suggest a more specific football question. Do not invent facts.",
        ),
        ("human", "Context:\n{context}\n\nQuestion: {question}"),
    ])
    document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    rag_chain = {
        "context": retriever,
        "question": RunnablePassthrough(),
    } | document_chain
    return rag_chain, retriever


def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap');

        :root {
            --pitch-green: #1f4d3a;
            --pitch-green-dark: #123325;
            --chalk: #f6f3ea;
            --card: #ffffff;
            --ink: #16211c;
            --muted: #5c6b62;
            --line: #e3ddcd;
            --accent: #d9622b;
            --accent-soft: #fbe4d3;
        }

        html, body, [class*="css"] { font-family: 'Manrope', sans-serif; }

        .stApp {
            background:
                radial-gradient(circle at 15% 0%, rgba(31,77,58,0.06), transparent 45%),
                var(--chalk);
        }

        .block-container { max-width: 980px; padding-top: 2rem; padding-bottom: 4rem; }

        /* ---- Hero ---- */
        .hero {
            position: relative;
            padding: 2.4rem 2.2rem;
            margin-bottom: 2rem;
            border-radius: 20px;
            background: linear-gradient(135deg, var(--pitch-green) 0%, var(--pitch-green-dark) 100%);
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(18,51,37,0.25);
        }
        .hero::before {
            content: "";
            position: absolute;
            inset: 0;
            background-image:
                repeating-linear-gradient(90deg, rgba(255,255,255,0.05) 0 2px, transparent 2px 64px);
            opacity: 0.6;
        }
        .hero::after {
            content: "";
            position: absolute;
            right: -60px; top: -60px;
            width: 220px; height: 220px;
            border: 2px solid rgba(255,255,255,0.12);
            border-radius: 50%;
        }
        .eyebrow {
            position: relative;
            display: inline-flex;
            align-items: center;
            gap: .5rem;
            color: var(--accent-soft);
            font-size: .74rem;
            font-weight: 700;
            letter-spacing: .14em;
            text-transform: uppercase;
        }
        .eyebrow::before { content: "\26BD"; font-size: 0.9rem; }
        .hero h1 {
            position: relative;
            font-family: 'Fraunces', serif;
            color: #fdfbf6;
            font-size: 2.9rem;
            font-weight: 600;
            line-height: 1.05;
            margin: .6rem 0 .5rem;
        }
        .hero p {
            position: relative;
            color: #cfe0d5;
            font-size: 1.02rem;
            max-width: 620px;
            margin: 0;
        }

        /* ---- Sidebar ---- */
        section[data-testid="stSidebar"] {
            background: var(--card);
            border-right: 1px solid var(--line);
        }
        section[data-testid="stSidebar"] .stButton button {
            border-radius: 10px;
            border: 1px solid var(--line);
            background: var(--chalk);
            color: var(--ink);
            font-size: 0.88rem;
            text-align: left;
            padding: 0.6rem 0.8rem;
            transition: all 0.15s ease;
        }
        section[data-testid="stSidebar"] .stButton button:hover {
            border-color: var(--accent);
            color: var(--accent);
            background: var(--accent-soft);
        }
        section[data-testid="stSidebar"] h3 {
            font-weight: 700;
            color: var(--ink);
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: .06em;
        }

        /* ---- Chat bubbles ---- */
        [data-testid="stChatMessage"] {
            border: 1px solid var(--line);
            border-radius: 14px;
            background: var(--card);
            padding: 0.4rem 0.2rem;
            box-shadow: 0 2px 8px rgba(18,51,37,0.04);
            margin-bottom: 0.6rem;
        }
        [data-testid="stChatMessageAvatarUser"] { background: var(--accent) !important; }
        [data-testid="stChatMessageAvatarAssistant"] { background: var(--pitch-green) !important; }

        [data-testid="stChatInput"] textarea {
            border-radius: 12px !important;
            border: 1px solid var(--line) !important;
        }

        /* ---- Expander (sources) ---- */
        details {
            border-radius: 10px !important;
            border: 1px dashed var(--line) !important;
            background: #fbfaf5;
        }
        summary {
            font-size: 0.85rem !important;
            color: var(--muted) !important;
            font-weight: 600 !important;
        }

        /* ---- Misc ---- */
        div[data-testid="stStatusWidget"], .stSpinner > div { color: var(--pitch-green) !important; }
        a { color: var(--accent) !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero():
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">Football knowledge base</div>
            <h1>Ask the game.</h1>
            <p>Explore football rules, history, competitions, and gameplay using a searchable reference source.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    st.set_page_config(page_title="Football RAG", page_icon="⚽", layout="wide")
    inject_css()
    render_hero()

    with st.sidebar:
        st.subheader("Try a question")
        suggestions = [
            "What is the offside rule?",
            "How long is a football match?",
            "How many players are on a team?",
            "What are the main football competitions?",
        ]
        for suggestion in suggestions:
            if st.button(suggestion, use_container_width=True):
                st.session_state.question = suggestion
        st.divider()
        st.link_button("⚽ Open the source", SOURCE_URL, use_container_width=True)
        if st.button("🗑️ Clear conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    st.session_state.setdefault("messages", [])
    st.session_state.setdefault("question", "")

    try:
        with st.spinner("Preparing the football knowledge base..."):
            rag_chain, retriever = build_rag_components()
    except RuntimeError as error:
        st.error(str(error))
        st.stop()

    for message in st.session_state.messages:
        avatar = "🧑" if message["role"] == "user" else "⚽"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
            if message.get("sources"):
                with st.expander("Sources used"):
                    for source in message["sources"]:
                        st.write(source)

    question = st.chat_input("Ask about football rules, history, or competitions")
    question = question or st.session_state.pop("question", "")
    if not question:
        return

    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(question)

    with st.chat_message("assistant", avatar="⚽"):
        with st.spinner("Searching the football source..."):
            answer = rag_chain.invoke(question)
            source_documents = retriever.invoke(question)
            sources = list(dict.fromkeys(
                document.metadata.get("source", SOURCE_URL)
                for document in source_documents
            ))
        st.markdown(answer)
        with st.expander("Sources used"):
            for source in sources:
                st.write(source)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources,
    })


if __name__ == "__main__":
    main()
