import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

gemini_model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def load_chunks(filepath, chunk_size=300):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def embed_chunks(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2') 
    embeddings = model.encode(chunks, convert_to_numpy=True)
    return embeddings

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def retrieve_chunks(query, chunks, index, embedder, k=3):
    query_embedding = embedder.encode([query], convert_to_numpy=True)
    D, I = index.search(query_embedding, k)
    return [chunks[i] for i in I[0]]

def generate_answer(context_chunks, query):
    context = "\n".join(context_chunks)
    prompt = f"""You are a helpful assistant. Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer:"""
    response = gemini_model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    chunks = load_chunks("document.txt")
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = embed_chunks(chunks)
    index = build_faiss_index(embeddings)

    print("🔍 Gemini RAG ready. Ask a question (type 'exit' to quit).")
    while True:
        question = input("\nYour question: ")
        if question.lower() == 'exit':
            break
        top_chunks = retrieve_chunks(question, chunks, index, embedder)
        answer = generate_answer(top_chunks, question)
        print("\n🧠 Gemini Answer:\n", answer)
