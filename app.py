import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFaceHub
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import HuggingFaceHub
from htmlTemplates import css, bot_template, user_template
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("""
You are a helpful assistant. Summarize the answer in 5-6 sentences.

Only respond with:
Helpful Answer (in 5-6 sentences): <your answer here>



Here is some context:
{context}

Question:
{question}

Helpful Answer (in 5-6 sentences):""")


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore



from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def get_conversation_chain(vectorstore):
    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=HuggingFaceHub(
            repo_id="mistralai/Mistral-7B-Instruct-v0.1",
            model_kwargs={
                "temperature": 0.7,
                "max_new_tokens": 300,
                "top_k": 50,
                "top_p": 0.95
            },
            task="text-generation"
        ),
        retriever=vectorstore.as_retriever(),
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt_template}
    )

    return chain


def handle_userinput(user_question):
    if st.session_state.conversation is not None:
        # Get response from conversation chain
        response = st.session_state.conversation({'question': user_question})
        full_answer = response['answer']

        # Extract only the content after "Helpful Answer (in 5-6 sentences):"
        helpful_answer = full_answer.split("Helpful Answer (in 5-6 sentences):")[-1].strip()

        # Display user question and the extracted bot response
        st.write(user_template.replace("{{MSG}}", user_question), unsafe_allow_html=True)
        st.write(bot_template.replace("{{MSG}}", helpful_answer), unsafe_allow_html=True)

        # Optional: store chat history
        st.session_state.chat_history = response.get("chat_history", [])
    else:
        st.warning("Please upload and process your PDFs first!")

    

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    st.header("Chat with multiple PDFs :books:")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    # Input box for user's question
    user_question = st.text_input("Ask a question about your documents:")

    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process") and pdf_docs:
            with st.spinner("Processing"):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)
            st.success("Documents processed! You can now ask questions.")


if __name__ == '__main__':
    main()


