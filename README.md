A Retrieval-Augmented Generation (RAG) chatbot that answers medical questions by grounding a large language model's responses in a private corpus of medical documents.

## Overview

Medical Chatbot is a Flask web application that lets a user ask health-related questions through a simple chat interface and receive answers generated from trusted medical source material rather than the language model's unguided knowledge. Source documents (PDFs) are chunked, embedded, and stored in a Pinecone vector database ahead of time by `store_index.py`. At query time, `app.py` retrieves the most relevant chunks for a user's question from Pinecone and passes them, along with the question, to a Groq-hosted Llama 3 model through a LangChain `RetrievalQA` chain, which returns a grounded answer to the browser.

## Key Features

- **Retrieval-augmented answers**: Responses are generated using context retrieved from indexed medical PDFs rather than the LLM's parametric knowledge alone, via LangChain's `RetrievalQA` chain.
- **Vector search over medical documents**: Document chunks are embedded and stored in a Pinecone index (`medical-chatbot`) for similarity search, retrieving the top-k (k=2) most relevant chunks per question.
- **Groq-hosted LLM inference**: Answers are generated using Groq's hosted Llama 3 (`Llama3-8b-8192`) through `langchain_groq.ChatGroq`, with a low temperature (0.4) for focused, factual responses.
- **Custom prompt template**: A dedicated prompt (`src/prompt.py`) instructs the model to answer only from the supplied context and to say it doesn't know rather than fabricate an answer.
- **PDF ingestion pipeline**: `store_index.py` and `src/helper.py` load all PDFs from a `data/` directory, split them into overlapping text chunks, embed them, and upload them to Pinecone.
- **Simple web chat UI**: A single-page chat interface (`templates/chat.html`, `static/css/style.css`) served by Flask, using jQuery to post messages to the backend and render responses without a page reload.

## Tech Stack

- **Web framework**: Flask
- **LLM orchestration**: LangChain (`langchain`, `langchain-community`), including `RetrievalQA` and `PromptTemplate`
- **LLM provider**: Groq, via `langchain-groq` (`ChatGroq`, model `Llama3-8b-8192`)
- **Vector store**: Pinecone, via `langchain-pinecone` (`PineconeVectorStore`) and `pinecone-client`
- **Embeddings**: HuggingFace `sentence-transformers/all-MiniLM-L6-v2`, via `langchain_community.embeddings.HuggingFaceEmbeddings` (backed by the `sentence-transformers` package)
- **Document loading and chunking**: `langchain_community.document_loaders` (`PyPDFLoader`, `DirectoryLoader`, backed by `pypdf`) and `langchain.text_splitter.RecursiveCharacterTextSplitter`
- **Configuration**: `python-dotenv` for loading environment variables from a `.env` file
- **Frontend**: HTML, CSS, and jQuery, with Bootstrap and Font Awesome loaded from a CDN

## Architecture

The project is split into an offline indexing step and an online serving step.

**Indexing (`store_index.py`)**

1. `load_pdf_file` (in `src/helper.py`) uses a LangChain `DirectoryLoader` with `PyPDFLoader` to load every PDF found in the local `data/` directory.
2. `text_split` splits the loaded documents into chunks of 500 characters with 20 characters of overlap using `RecursiveCharacterTextSplitter`, so retrieval can operate on small, focused passages instead of whole documents.
3. `download_hugging_face_embeddings` loads the `sentence-transformers/all-MiniLM-L6-v2` embedding model.
4. The chunks and their embeddings are uploaded to a Pinecone index named `medical-chatbot` via `PineconeVectorStore.from_documents`. The Pinecone index itself must already exist (created in the Pinecone dashboard or API with a dimension matching the embedding model, 384 for MiniLM) before this script is run.

**Serving (`app.py`)**

1. On startup, the Flask app loads `PINECONE_API_KEY` and `GROQ_API_KEY` from the environment (via `.env`), initializes the same HuggingFace embedding model used at indexing time, and connects to the existing `medical-chatbot` Pinecone index with `PineconeVectorStore.from_existing_index`.
2. A `PromptTemplate` (`src/prompt.py`) is combined with a `ChatGroq` LLM (`Llama3-8b-8192`) into a LangChain `RetrievalQA` chain, configured to retrieve the top 2 most similar chunks (`search_kwargs={'k': 2}`) for each question and return the source documents alongside the answer.
3. The `/` route renders the chat UI (`templates/chat.html`).
4. The `/get` route receives the user's message from the chat form, runs it through the `RetrievalQA` chain, and returns the generated answer as plain text, which the frontend JavaScript appends to the chat window.

## Setup / Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mahnooramjad05/Medical-Chatbot.git
   cd Medical-Chatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy the example file and fill in your own API keys:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and set `PINECONE_API_KEY` and `GROQ_API_KEY` (see [Environment Variables](#environment-variables) below).

5. **Add source documents and build the Pinecone index**

   Create a `data/` directory in the project root and place your medical PDF(s) inside it. Make sure a Pinecone index named `medical-chatbot` already exists (dimension 384, to match the MiniLM embedding model), then run:
   ```bash
   python store_index.py
   ```
   This loads, chunks, embeds, and uploads the PDF content to Pinecone.

6. **Run the application**
   ```bash
   python app.py
   ```
   The app starts on `http://0.0.0.0:8080` (accessible locally at `http://localhost:8080`) in debug mode.

## Usage

1. Open `http://localhost:8080` in a web browser once the app is running.
2. Type a question into the chat input at the bottom of the page, for example:
   ```
   What are the common symptoms of diabetes?
   ```
3. Press send (or hit Enter). The message is posted to the `/get` endpoint, which retrieves the most relevant chunks from the indexed medical documents and returns an answer generated by the Groq-hosted Llama 3 model, grounded in that retrieved context.
4. If the indexed documents don't contain information relevant to the question, the model is instructed (via the prompt template) to say it doesn't know rather than invent an answer.

## Environment Variables

Environment variables are loaded from a `.env` file at startup (see `.env.example`):

| Variable | Description |
|---|---|
| `PINECONE_API_KEY` | API key for your Pinecone account, used to connect to and query the `medical-chatbot` vector index. |
| `GROQ_API_KEY` | API key for Groq, used to run inference against the hosted Llama 3 (`Llama3-8b-8192`) model via `langchain_groq.ChatGroq`. |

Neither key is committed to the repository; only placeholder values are provided in `.env.example`. Create your own `.env` file locally (it is excluded from version control) and populate it with your real keys before running `store_index.py` or `app.py`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
