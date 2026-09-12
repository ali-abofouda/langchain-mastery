import os
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


def build_rag_chain():
    load_dotenv(find_dotenv())

    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError("GROQ_API_KEY is not set in the environment or .env file.")

    documents = WebBaseLoader(SOURCE_URL).load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
    vector_store = FAISS.from_documents(chunks, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.7,
        max_tokens=800,
    )
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Answer the question using only the provided football context. "
            "If the answer is not in the context, say you do not know.",
        ),
        ("human", "Context:\n{context}\n\nQuestion: {question}"),
    ])
    document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)

    return (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
        | document_chain
    )


def main():
    print("Building the football knowledge base...")
    rag_chain = build_rag_chain()
    print("Ready. Ask a football question, or type 'exit' to quit.")

    while True:
        question = input("\nQuestion: ").strip()
        if question.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break
        if not question:
            continue

        answer = rag_chain.invoke(question)
        print(f"\nAnswer:\n{answer}")


if __name__ == "__main__":
    main()
