from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# 1. Load the PDF
extracted_data = load_pdf_file(data_path='data/')

# 2. Split the PDF into Chunks
text_chunks = text_split(extracted_data)

# 3. Download Embeddings
embeddings = download_hugging_face_embeddings()

# 4. Create and Upload the Index to Pinecone
index_name = "medical-chatbot"

# Use the PineconeVectorStore to create the index
# Note: You must have already created an index named "medical-chatbot" in your Pinecone dashboard with correct dimensions (384 for MiniLM).
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

print("Indexing complete. Data uploaded to Pinecone.")
