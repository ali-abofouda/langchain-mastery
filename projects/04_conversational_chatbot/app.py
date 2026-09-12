import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv(find_dotenv())

# إعداد خادم المحادثة والذاكرة
if "store" not in st.session_state:
    st.session_state.store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = ChatMessageHistory()
    return st.session_state.store[session_id]


@st.cache_resource(show_spinner=False)
def build_chat_chain():
    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError("GROQ_API_KEY is not set in the environment or .env file.")

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.4,
        max_tokens=800,
    )
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a friendly, highly intelligent AI assistant built with LangChain. "
            "Always maintain context from past messages and answer helpful and accurately in the user's language.",
        ),
        MessagesPlaceholder(variable_name="messages"),
        ("human", "{question}"),
    ])
    chain = prompt | llm

    return RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="question",
        history_messages_key="messages",
    )


def main():
    st.set_page_config(page_title="Conversational Chatbot", page_icon="💬", layout="wide")
    st.title("💬 Smart Conversational Assistant (Memory & Chat History)")

    # Sidebar for Sessions Management
    with st.sidebar:
        st.header("⚙️ Session Controls")
        session_id = st.text_input("Session ID:", value="default_session")
        st.caption("Each session ID preserves its own memory history independently.")

        if st.button("🗑️ Clear Session Memory", use_container_width=True):
            if session_id in st.session_state.store:
                st.session_state.store[session_id].clear()
                st.success(f"Cleared memory for session: {session_id}")
                st.rerun()

    try:
        chat_chain = build_chat_chain()
    except RuntimeError as e:
        st.error(str(e))
        st.stop()

    # Get current session's history
    history = get_session_history(session_id)

    # Render previous messages from history
    for msg in history.messages:
        role = "user" if msg.type == "human" else "assistant"
        avatar = "🧑" if role == "user" else "🤖"
        with st.chat_message(role, avatar=avatar):
            st.markdown(msg.content)

    # Chat Input
    question = st.chat_input("Type your message here...")
    if question:
        # Display user message immediately
        with st.chat_message("user", avatar="🧑"):
            st.markdown(question)

        config = {"configurable": {"session_id": session_id}}

        # Stream assistant response
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Thinking..."):
                response = chat_chain.invoke({"question": question}, config=config)
                st.markdown(response.content)

        st.rerun()


if __name__ == "__main__":
    main()
