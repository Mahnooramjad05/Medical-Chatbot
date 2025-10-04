🧠 Medical Chatbot
An intelligent Medical Chatbot built with Flask, LangChain, Pinecone, and Groq LLM, designed to answer health-related questions using retrieval-augmented generation (RAG).
This system leverages Hugging Face embeddings and a Pinecone vector database to fetch the most relevant medical information and generate accurate, context-aware responses.

🚀 Features
🩺 Medical Q&A System – Answers user questions based on medical documents or indexed data.
⚙️ RAG Pipeline – Combines document retrieval and LLM reasoning for fact-based answers.
🧩 Pinecone Vector Store Integration – Stores and retrieves medical embeddings efficiently.
🤖 Groq Llama 3.1 Model – Generates coherent and contextually relevant responses.
🌐 Flask Web App – Simple web interface for chat interaction (chat.html).
🔒 Environment Secure – Uses .env for managing API keys securely.
🧱 Tech Stack

Component	Description
Flask	Web framework for serving the chatbot UI and API
LangChain	Framework for chaining LLM and retrieval logic
Groq (Llama 3.1-8B Instant)	Language model used for response generation
Pinecone	Vector database for semantic search and retrieval
Hugging Face Embeddings	Used to convert text documents into vector form
HTML / JS	Frontend for user chat interface
⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/medical-chatbot.git
cd medical-chatbot

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3. Install Dependencies
pip install -r requirements.txt

4. Set Up Environment Variables
Create a .env file in the root directory:
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key

5. Run the Flask App
python app.py


Visit the app in your browser at:
http://localhost:8080
🧩 Project Structure
medical-chatbot/
│
├── src/
│   ├── helper.py             # Handles embeddings and vector store setup
│   ├── prompt.py             # Contains the system prompt and templates
│
├── templates/
│   └── chat.html             # Web UI for chatting with the bot
│
├── app.py                    # Main Flask application
├── .env                      # Environment variables
├── requirements.txt          # Dependencies
└── README.md                 # Documentation

🧠 How It Works
Embedding Generation:
Medical documents are embedded using Hugging Face embeddings.
Vector Storage:
Embeddings are stored in a Pinecone index (medical-chatbot).
Retrieval:
When a user asks a question, the system retrieves the top 3 (k=3) relevant chunks.
Response Generation:
The retrieved context is passed to Llama 3.1 through LangChain for generating the final medical answer.

🧾 Example Query
User: “What are the symptoms of hypertension?”
Bot: “Common symptoms of hypertension include headaches, shortness of breath, dizziness, or nosebleeds. However, it is often asymptomatic and requires regular monitoring.”

⚠️ Disclaimer
This chatbot is for educational and informational purposes only.
It is not a substitute for professional medical advice, diagnosis, or treatment.
Always consult a qualified healthcare provider for any medical concerns.

📧 Contact
Developer: Mahnoor Amjad
Field: AI/ML | NLP | Deep Learning | Data Science
