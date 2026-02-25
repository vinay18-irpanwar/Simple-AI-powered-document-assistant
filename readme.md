📄 AI-Powered PDF Research Assistant

An intelligent Retrieval-Augmented Generation (RAG) application built with Streamlit + LangChain + Gemini + FAISS.

Upload any PDF document and ask questions — the AI will answer strictly based on the document content.

🚀 Features

📂 Upload PDF documents

🔎 Semantic search using FAISS

🧠 Context-aware answers using Gemini

📌 Clean and interactive Streamlit UI

⚡ Fast embeddings using sentence-transformers

🔐 Secure API key management with .env

🏗️ Tech Stack

Frontend: Streamlit

LLM: Gemini (via LangChain)

Embeddings: sentence-transformers

Vector Store: FAISS

Document Loader: PyMuPDF

Framework: LangChain

📂 Project Structure
AI-PDF-Research-Assistant/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
🔐 Setup API Key

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_api_key_here
⚙️ Installation
1️⃣ Create Virtual Environment
python -m venv venv
2️⃣ Activate Environment

Windows (PowerShell):

.\venv\Scripts\Activate.ps1

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py

The app will open in your browser at:

http://localhost:8501
🧠 How It Works

User uploads a PDF.

Document is loaded using PyMuPDF.

Text is split into chunks.

Chunks are converted into embeddings.

FAISS stores embeddings for semantic search.

Relevant chunks are retrieved.

Gemini generates an answer based only on retrieved context.

🎯 Example Use Case

Upload:

Research papers

Project reports

Academic notes

Technical documentation

Ask:

"What is the main objective?"

"Summarize chapter 3"

"Explain the methodology"

📦 Requirements
streamlit
langchain
langchain-community
langchain-google-genai
faiss-cpu
pymupdf
sentence-transformers
python-dotenv
🛠️ Future Improvements

Conversational chat memory

Multi-PDF support

Source citation display

Persistent vector database

Deployment on Streamlit Cloud


