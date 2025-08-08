# 🤖 Gemini-Powered RAG Assistant

A powerful Retrieval-Augmented Generation (RAG) pipeline that uses FAISS, Sentence Transformers, and Google Gemini 1.5 Pro to answer natural language questions using external documents as knowledge base.

---

## 📂 Project Overview

This project performs:

1. ✅ Chunking of large documents  
2. ✅ Embedding using `sentence-transformers`  
3. ✅ Fast vector search via `FAISS`  
4. ✅ Response generation using **Gemini 1.5 Pro** with context

---

## 🚀 How It Works

1. Loads and splits `document.txt` into 300-character chunks  
2. Generates embeddings for each chunk using `all-MiniLM-L6-v2`  
3. Stores embeddings in a FAISS index  
4. At runtime:
   - Embeds the user query
   - Retrieves top-k most relevant chunks
   - Constructs a context-enhanced prompt
   - Sends prompt to Gemini for answer generation

---

## 📁 Project Files

```
.
├── app.py               # Main script (RAG pipeline)
├── .env                 # API key for Gemini
├── document.txt         # The external knowledge base
└── README.md            # Project description (this file)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/rag-gemini-assistant.git
cd rag-gemini-assistant
```

### 2. Create and configure `.env`

```env
GOOGLE_API_KEY=your_api_key_here
```

> You can get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app)

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure `requirements.txt` includes:
```txt
numpy
faiss-cpu
sentence-transformers
google-generativeai
python-dotenv
```

---

## 🧠 How to Run

```bash
python app.py
```

Then interact via command-line:

```
🔍 Gemini RAG ready. Ask a question (type 'exit' to quit).
Your question: What is reinforcement learning?

🧠 Gemini Answer:
Reinforcement learning is a type of machine learning where agents learn to make decisions by interacting with their environment and receiving rewards or penalties...
```

---

## 🧪 Example Questions

Try asking:

- "What is the role of CNNs in deep learning?"
- "List key challenges in AI safety"
- "What are transformer models used for?"

---

## 📦 Technologies Used

- 🧠 [Google Gemini 1.5 Pro](https://ai.google.dev/)
- 🧮 [FAISS](https://github.com/facebookresearch/faiss)
- 💬 [Sentence Transformers](https://www.sbert.net/)
- 🧾 [dotenv](https://pypi.org/project/python-dotenv/)
- 🐍 Python 3.9+

---

## 🔐 Notes

- Your `.env` file is **excluded** from Git tracking for security
- Gemini model is called via Google GenerativeAI API, not locally

---

## 📌 Future Improvements

- Add web UI (Streamlit, Flask, Gradio)
- Support PDF/document loaders
- Save chat history
- Add source highlighting for each chunk

---

## 🧑‍💻 Author

**Mahmoud Elnahrawy**  
Email: mahmoudelnahrawywork@gmail.com
Location: Cairo, Egypt

---

## 🪪 License

MIT License. Free to use, modify, and distribute.
