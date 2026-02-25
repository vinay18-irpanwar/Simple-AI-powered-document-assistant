# 📄 AI-Powered PDF Research Assistant

An intelligent **Retrieval-Augmented Generation (RAG)** web application built using **Streamlit, LangChain, Gemini, and FAISS**.

Upload any PDF document and ask questions — the AI answers strictly based on the document content.

---

## 🚀 Features

- 📂 Upload any PDF document  
- 🔎 Semantic search using FAISS  
- 🧠 Context-aware answers using Gemini (LLM)  
- 📑 Smart document chunking  
- ⚡ Fast embeddings using sentence-transformers  
- 🎨 Clean and interactive Streamlit UI  
- 🔐 Secure API key management  

---

## 🏗️ Tech Stack

| Component        | Technology |
|------------------|------------|
| Frontend         | Streamlit |
| LLM              | Gemini (Google Generative AI) |
| Framework        | LangChain |
| Embeddings       | sentence-transformers |
| Vector Database  | FAISS |
| PDF Loader       | PyMuPDF |

---

## 📂 Project Structure


AI-PDF-Research-Assistant/
│
├── app.py
├── requirements.txt
├── .env
└── README.md


---

## 🔐 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/AI-PDF-Research-Assistant.git
cd AI-PDF-Research-Assistant
2️⃣ Create Virtual Environment
python -m venv venv

Activate the environment:

Windows

.\venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add Gemini API Key

Create a .env file in the root directory:

GOOGLE_API_KEY=your_api_key_here
▶️ Run the Application
streamlit run app.py

Then open:

http://localhost:8501
🧠 How It Works (RAG Pipeline)

User uploads a PDF.

PDF text is extracted using PyMuPDF.

Text is split into smaller chunks.

Chunks are converted into embeddings.

FAISS stores embeddings for semantic search.

Relevant chunks are retrieved based on the query.

Gemini generates a response using retrieved context only.

📌 Example Questions

Summarize the document

What is the main objective?

Explain the methodology

Compare advantages and disadvantages

What conclusion is drawn?

📦 Requirements

streamlit

langchain

langchain-community

langchain-google-genai

faiss-cpu

pymupdf

sentence-transformers

python-dotenv

⚠️ Note

On first run, the embedding model (~90MB) will download automatically.
Subsequent runs will load instantly from cache.

🔮 Future Improvements

Multi-PDF support

Conversational chat mode

Source citation display

Persistent vector storage

Deployment on Streamlit Cloud
