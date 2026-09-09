# Football RAG Application

This project is a small retrieval-augmented generation (RAG) application about association football.

## Project Components

- `streamlit_app.py`: Interactive web application with chat history and source links.
- `app.py`: Interactive command-line application.
- `football_rag_app.ipynb`: Step-by-step notebook version of the same pipeline.

## How It Works

1. Loads football content from Wikipedia.
2. Splits the content into overlapping text chunks.
3. Creates local HuggingFace embeddings.
4. Stores the embeddings in a FAISS vector store.
5. Retrieves the most relevant chunks for each question.
6. Sends the retrieved context to a Groq chat model.
7. Prints an answer based on the retrieved content.

## Requirements

- Python 3.12 or newer.
- A `GROQ_API_KEY` set in the project `.env` file or environment.
- Dependencies installed with `uv sync`.

Example `.env` entry:

```text
GROQ_API_KEY=your-groq-api-key
```

## Run the Web Application

From the repository root, run:

```bash
uv run streamlit run projects/football_rag/streamlit_app.py
```

The interface provides suggested questions, conversation history, a clear button, and expandable source links.

The assistant answers in the same language as the question. It uses five retrieved chunks instead of relying on a single result, and it explains when the source does not contain enough information.

## Run the Command-Line Application

From the repository root, run:

```bash
uv run python projects/football_rag/app.py
```

The application builds the knowledge base and then accepts questions such as:

```text
What is the offside rule?
How long is a standard football match?
How many players are on a football team?
```

Type `exit` or `quit` to close the application.

## Run the Notebook

Open `football_rag_app.ipynb` in VS Code and execute the cells in order. The notebook shows each stage of the pipeline separately, which makes it useful for learning and experimentation.

## Future Extensions

The project can later be extended with a web interface, persistent vector storage, multiple football sources, conversation history, or support for Arabic questions.
