# 🤖 Gemini-Powered RAG Assistant
A **Retrieval-Augmented Generation (RAG)** pipeline combining **FAISS**, **Sentence Transformers**, and **Google Gemini 1.5 Pro** to answer natural language questions using your own knowledge base.

---

## 📌 Features
- 📄 Automatic **chunking** of large documents  
- 🧮 High-quality **embeddings** with `sentence-transformers`  
- ⚡ Ultra-fast **vector search** via FAISS  
- 🤖 **Context-aware answers** using Google Gemini 1.5 Pro  

---

## 🗂 Project Structure
.
├── app.py               # Main RAG pipeline script
├── .env                 # API key (not tracked by Git)
├── document.txt         # Example knowledge base
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

---

## ⚙️ Installation

### 1️⃣ Clone the repository
git clone https://github.com/NA7RAWY/Gemini-Powered-RAG-Assistant.git
cd Gemini-Powered-RAG-Assistant

### 2️⃣ Set up environment variables
Create a `.env` file:
GOOGLE_API_KEY=your_api_key_here
Get your API key from [Google AI Studio](https://makersuite.google.com/app).

### 3️⃣ Install dependencies
pip install -r requirements.txt
Dependencies:
numpy
faiss-cpu
sentence-transformers
google-generativeai
python-dotenv

---

## 🚀 How It Works
1. **Chunking** — Splits `document.txt` into 300-character segments  
2. **Embedding** — Generates embeddings using `all-MiniLM-L6-v2`  
3. **Indexing** — Stores embeddings in FAISS for fast search  
4. **Query Flow**:
   - Embed the user query
   - Retrieve the top-k relevant chunks
   - Build a context-rich prompt
   - Send it to Gemini for a final answer

---

## 🧠 Usage
Run the script:
python app.py

Example:
🔍 Gemini RAG ready. Ask a question (type 'exit' to quit').
Your question: What is reinforcement learning?

🧠 Gemini Answer:
Reinforcement learning is a type of machine learning where agents learn to make decisions by interacting with their environment and receiving rewards or penalties...

---

## 💡 Example Queries
- "What is the role of CNNs in deep learning?"
- "List key challenges in AI safety"
- "What are transformer models used for?"

---

## 🛠 Tech Stack
- 🧠 [Google Gemini 1.5 Pro](https://ai.google.dev/)
- 🧮 [FAISS](https://github.com/facebookresearch/faiss)
- 💬 [Sentence Transformers](https://www.sbert.net/)
- 🧾 [dotenv](https://pypi.org/project/python-dotenv/)
- 🐍 Python 3.9+

---

## 🔮 Roadmap
- [ ] Add web UI (Streamlit / Flask / Gradio)  
- [ ] PDF & multiple file loaders  
- [ ] Persistent chat history  
- [ ] Chunk source highlighting  

---

## 👤 Author
**Mahmoud Elnahrawy**  
📧 [mahmoudelnahrawywork@gmail.com](mailto:mahmoudelnahrawywork@gmail.com)  
📍 Cairo, Egypt  

---

## 🪪 License
MIT License — free to use, modify, and distribute.
