

# 📚 Chat with Multiple PDFs

This project is a **Streamlit web app** that allows users to interactively **chat with multiple PDF documents** using **natural language queries**. It uses **LangChain**, **FAISS**, **Hugging Face Embeddings**, and a **LLM (Mistral-7B-Instruct)** to provide intelligent, context-aware answers from the uploaded documents.

---

## 🚀 Features

- 🧠 Uses **Mistral 7B Instruct** via Hugging Face for accurate language generation.
- 📄 Supports **multiple PDF uploads**.
- 📌 Intelligent **question answering** using conversational memory.
- ✂️ PDF content is split into **text chunks** for efficient vector search.
- 🔍 Uses **FAISS** for fast vector similarity search.
- 💬 Styled chat interface with **custom HTML/CSS** templates.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM**: Mistral-7B-Instruct (via Hugging Face Hub)
- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`
- **Vector DB**: FAISS
- **PDF Parsing**: PyPDF2
- **Framework**: LangChain

---

## 📂 File Structure

```
├── app.py                # Main Streamlit app
├── htmlTemplates.py      # Custom chat UI with CSS and HTML templates
```

---

## 🧪 How It Works

1. **Upload PDFs** using the sidebar.
2. Click **"Process"** to extract and index the text.
3. Ask **natural language questions** about your PDFs.
4. The app uses an **LLM** with context-aware retrieval to generate summaries.
5. Responses are displayed in a styled chat format.

---
## How it looks!

<img width="1470" alt="Screenshot 2025-04-15 at 2 16 06 PM" src="https://github.com/user-attachments/assets/8704de37-c7c1-4e9d-a785-5f4d103c26f6" />
<img width="1470" alt="Screenshot 2025-04-15 at 2 15 53 PM" src="https://github.com/user-attachments/assets/fa23987e-3c69-43e0-b143-57ab878bdb64" />

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Hugging Face](https://huggingface.co/)
- [FAISS](https://github.com/facebookresearch/faiss)

---
