# Medical Chatbot AI 🏥

An intelligent Medical Chatbot that uses **RAG (Retrieval-Augmented Generation)** to answer health-related questions based on trusted medical literature. Built with LangChain, Pinecone, and Groq (Llama 3).

## 🚀 Features
- **Accurate Responses**: Answers questions based on private medical data (PDFs).
- **Fast Generation**: Powered by Groq's LPU for near-instant responses.
- **Persistent Memory**: Uses Pinecone Vector Database for efficient information retrieval.
- **Modern UI**: Clean and responsive web interface built with Flask and Bootstrap.

## 🛠️ Tech Stack
- **LLM**: Groq (Llama3-8b)
- **Framework**: LangChain, Flask
- **Vector Store**: Pinecone
- **Embeddings**: HuggingFace (MiniLM-L6)
- **Frontend**: HTML/CSS, JavaScript (jQuery)

## 📁 Project Structure
```text
Medical-Chatbot/
├── src/                # Utility modules
│   ├── helper.py       # Data loading & processing
│   └── prompt.py       # System instructions
├── static/css/         # UI Styles
├── templates/          # HTML Templates
├── data/               # Medical PDF source (add your PDF here)
├── .env.example        # API Key template
├── app.py              # Main Flask application
├── requirements.txt    # Dependencies
└── store_index.py      # Script to ingest data into Pinecone
```

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Mahnooramjad05/Medical-Chatbot.git
cd Medical-Chatbot
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file from the example:
```bash
cp .env.example .env
```
Fill in your `PINECONE_API_KEY` and `GROQ_API_KEY`.

### 5. Ingest Data
Place your medical PDF in the `data/` folder, then run:
```bash
python store_index.py
```

### 6. Run the App
```bash
python app.py
```
Visit `http://localhost:8080` in your browser.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Developed with ❤️ by [Mahnoor Amjad](https://github.com/Mahnooramjad05)
