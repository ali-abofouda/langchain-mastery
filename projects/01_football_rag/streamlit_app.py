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


def inject_custom_dark_theme():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Cabinet+Grotesk:wght@700;800;900&display=swap');

        :root {
            --bg-dark: #090d0b;
            --card-dark: #111a15;
            --card-border: #1d2e25;
            --pitch-green: #00e676;
            --pitch-green-glow: rgba(0, 230, 118, 0.25);
            --gold-accent: #ffc107;
            --gold-glow: rgba(255, 193, 7, 0.2);
            --text-main: #f0f7f4;
            --text-muted: #8ca398;
            --user-bubble: #15291f;
            --assistant-bubble: #0f1c16;
        }

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: var(--text-main);
            background-color: var(--bg-dark);
        }

        .stApp {
            background: 
                radial-gradient(circle at 50% -10%, rgba(0, 230, 118, 0.08), transparent 45%),
                radial-gradient(circle at 85% 60%, rgba(255, 193, 7, 0.04), transparent 40%),
                var(--bg-dark);
        }

        .block-container {
            max-width: 1000px;
            padding-top: 2rem;
            padding-bottom: 5rem;
        }

        /* ---- Hero Section (Dark Mode Pitch) ---- */
        .hero-dark {
            position: relative;
            padding: 2.6rem 2.4rem;
            margin-bottom: 2.2rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #0e2117 0%, #06120b 100%);
            border: 1px solid rgba(0, 230, 118, 0.25);
            overflow: hidden;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }

        .hero-dark::before {
            content: "";
            position: absolute;
            inset: 0;
            background-image: 
                repeating-linear-gradient(90deg, rgba(0, 230, 118, 0.03) 0 2px, transparent 2px 70px),
                repeating-linear-gradient(0deg, rgba(0, 230, 118, 0.03) 0 2px, transparent 2px 70px);
            opacity: 0.7;
        }

        .hero-dark::after {
            content: "";
            position: absolute;
            right: -80px;
            top: -80px;
            width: 280px;
            height: 280px;
            border: 2px solid rgba(0, 230, 118, 0.15);
            border-radius: 50%;
            pointer-events: none;
        }

        .eyebrow-badge {
            position: relative;
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            padding: 0.35rem 0.85rem;
            border-radius: 30px;
            background: rgba(0, 230, 118, 0.12);
            border: 1px solid rgba(0, 230, 118, 0.3);
            color: var(--pitch-green);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            box-shadow: 0 0 15px var(--pitch-green-glow);
        }

        .hero-dark h1 {
            position: relative;
            font-family: 'Cabinet Grotesk', sans-serif;
            color: #ffffff;
            font-size: 3.2rem;
            font-weight: 900;
            line-height: 1.05;
            margin: 0.8rem 0 0.6rem;
            letter-spacing: -0.02em;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }

        .hero-dark p {
            position: relative;
            color: var(--text-muted);
            font-size: 1.08rem;
            max-width: 650px;
            margin: 0;
            line-height: 1.6;
        }

        /* ---- Sidebar Styling (Dark Mode) ---- */
        section[data-testid="stSidebar"] {
            background-color: var(--card-dark) !important;
            border-right: 1px solid var(--card-border) !important;
        }

        section[data-testid="stSidebar"] .stButton button {
            border-radius: 12px;
            border: 1px solid var(--card-border);
            background: rgba(255, 255, 255, 0.03);
            color: var(--text-main);
            font-size: 0.88rem;
            font-weight: 500;
            text-align: left;
            padding: 0.65rem 0.9rem;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }

        section[data-testid="stSidebar"] .stButton button:hover {
            border-color: var(--pitch-green);
            color: var(--pitch-green);
            background: rgba(0, 230, 118, 0.08);
            box-shadow: 0 0 12px var(--pitch-green-glow);
            transform: translateY(-1px);
        }

        section[data-testid="stSidebar"] h3 {
            font-weight: 800;
            color: var(--pitch-green);
            font-size: 0.88rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }

        /* ---- Chat Messages ---- */
        [data-testid="stChatMessage"] {
            border: 1px solid var(--card-border);
            border-radius: 16px;
            background: var(--card-dark);
            padding: 0.6rem 0.8rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            margin-bottom: 0.8rem;
            backdrop-filter: blur(10px);
        }

        [data-testid="stChatMessageAvatarUser"] {
            background: linear-gradient(135deg, var(--gold-accent), #d48806) !important;
            color: #000000 !important;
            font-weight: bold;
        }

        [data-testid="stChatMessageAvatarAssistant"] {
            background: linear-gradient(135deg, var(--pitch-green), #00a854) !important;
            color: #000000 !important;
            box-shadow: 0 0 12px var(--pitch-green-glow);
        }

        /* ---- Chat Input Bar ---- */
        [data-testid="stChatInput"] {
            background-color: transparent !important;
        }

        [data-testid="stChatInput"] textarea {
            border-radius: 14px !important;
            border: 1px solid var(--card-border) !important;
            background-color: var(--card-dark) !important;
            color: var(--text-main) !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4) !important;
            font-size: 0.95rem !important;
        }

        [data-testid="stChatInput"] textarea:focus {
            border-color: var(--pitch-green) !important;
            box-shadow: 0 0 15px var(--pitch-green-glow) !important;
        }

        /* ---- Expanders (Sources) ---- */
        details {
            border-radius: 12px !important;
            border: 1px solid var(--card-border) !important;
            background: rgba(0, 0, 0, 0.25) !important;
            padding: 0.2rem 0.5rem;
        }

        summary {
            font-size: 0.85rem !important;
            color: var(--text-muted) !important;
            font-weight: 600 !important;
        }

        summary:hover {
            color: var(--pitch-green) !important;
        }

        /* ---- Links & Divider ---- */
        a {
            color: var(--pitch-green) !important;
            text-decoration: none !important;
            font-weight: 600;
        }

        a:hover {
            text-decoration: underline !important;
        }

        hr {
            border-color: var(--card-border) !important;
        }

        /* ---- Spinners & Status ---- */
        div[data-testid="stStatusWidget"], .stSpinner > div {
            color: var(--pitch-green) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_dark_hero():
    st.markdown(
        """
        <div class="hero-dark">
            <div class="eyebrow-badge">⚽ Football Knowledge RAG System</div>
            <h1>Ask the Game.</h1>
            <p>Explore football rules, history, competitions, and tactical regulations powered by modern AI vector search.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    st.set_page_config(page_title="Football RAG - Dark Mode", page_icon="⚽", layout="wide")
    inject_custom_dark_theme()
    render_dark_hero()

    with st.sidebar:
        st.subheader("💡 Suggested Questions")
        suggestions = [
            "What is the offside rule?",
            "How long is a standard football match?",
            "How many players are on a football team?",
            "What are the main football competitions?",
        ]
        for suggestion in suggestions:
            if st.button(suggestion, use_container_width=True):
                st.session_state.question = suggestion

        st.divider()
        st.link_button("🌐 Open Wikipedia Source", SOURCE_URL, use_container_width=True)

        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    st.session_state.setdefault("messages", [])
    st.session_state.setdefault("question", "")

    try:
        with st.spinner("⚡ Initializing vector store & Groq LLM..."):
            rag_chain, retriever = build_rag_components()
    except RuntimeError as error:
        st.error(str(error))
        st.stop()

    # Render Chat History
    for message in st.session_state.messages:
        avatar = "🧑" if message["role"] == "user" else "⚽"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
            if message.get("sources"):
                with st.expander("📚 Sources Used"):
                    for source in message["sources"]:
                        st.write(source)

    # Handle Input Question
    question = st.chat_input("Ask any football question in English or Arabic...")
    question = question or st.session_state.pop("question", "")
    if not question:
        return

    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(question)

    with st.chat_message("assistant", avatar="⚽"):
        with st.spinner("⚽ Searching knowledge base..."):
            answer = rag_chain.invoke(question)
            source_documents = retriever.invoke(question)
            sources = list(dict.fromkeys(
                document.metadata.get("source", SOURCE_URL)
                for document in source_documents
            ))
        st.markdown(answer)
        with st.expander("📚 Sources Used"):
            for source in sources:
                st.write(source)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources,
    })


if __name__ == "__main__":
    main()
