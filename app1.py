import streamlit as st
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS


# ------------------- CONFIG -------------------
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(
    page_title="📄 AI PDF Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# ------------------- UI HEADER -------------------
st.title("📄 AI-Powered PDF Research Assistant")
st.markdown("Upload a PDF and ask questions. The AI will answer based only on the document.")

# ------------------- MODEL -------------------
@st.cache_resource
def load_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY
    )

@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

model = load_model()
embeddings = load_embeddings()

# ------------------- SIDEBAR -------------------
with st.sidebar:
    st.header("⚙️ Settings")
    st.info("Make sure your GOOGLE_API_KEY is set in .env file")
    st.markdown("Built using LangChain + Gemini + FAISS")

# ------------------- FILE UPLOAD -------------------
uploaded_file = st.file_uploader("📂 Upload your PDF file", type=["pdf"])

query = st.text_input("💬 Ask your question about the PDF")

# ------------------- MAIN LOGIC -------------------
def run_rag(query, uploaded_file):

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    loader = PyMuPDFLoader("temp.pdf")
    content = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(content)

    vector_store = FAISS.from_documents(chunks, embeddings)

    search_results = vector_store.similarity_search(query, k=4)

    context = [doc.page_content for doc in search_results]

    RAG_PROMPT = f"""
    You are an advanced AI Document Analysis Assistant.

Your role:
- Carefully analyze the provided context from a document.
- Answer the user's question strictly using the given context.


Response Guidelines:
- Be clear, precise, and structured.
- Use bullet points if helpful.
- If the user asks for explanation → explain step-by-step.
- If the user asks for summary → provide concise summary.
- If the user asks for comparison → present comparison in table format.
- If the user asks for definition → give exact definition from context.
- If numerical data exists → include exact values.

Context:
{context}

User Question:
{query}

Answer:
"""

    response = model.invoke(RAG_PROMPT)
    return response.content


# ------------------- BUTTON -------------------
if st.button("🚀 Generate Answer"):

    if uploaded_file is None:
        st.warning("Please upload a PDF file first.")
    elif not query:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing document..."):
            answer = run_rag(query, uploaded_file)

        st.success("Answer Generated!")
        st.markdown("### 📌 Answer")
        st.write(answer)