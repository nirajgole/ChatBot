from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from ollama import chat
import streamlit as st

# load the document
docs = PyPDFLoader("data/Big_O_Notes.pdf").load()

# split the document into chunks
#chunk_size should be greater than chunk_overlap
splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=1500)
chunks = splitter.split_documents(docs)

# create the embedding model
embedding_model = OllamaEmbeddings(model="llama3.2:latest")
vector_store = Chroma.from_documents(
    chunks, embedding_model, persist_directory="chroma_db"
)


# retrieve the most relevant chunks from the vector store
def retrieve(query: str) -> str:
    return vector_store.similarity_search(query, k=3)


def generate_answer(query: str, context: str) -> str:
    response = chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": "Answer the questions based on the provided context.\n\nContext:{context}",
            },
            {
                "role": "user",
                "content": query,
            },
        ],
    )
    return response["message"]["content"]


st.title("AZ900 RAG with Ollama and Chroma")
user_query = st.text_input("Enter your question about AZ900:")

if user_query:
    with st.spinner("Generating answer..."):
        context = retrieve(user_query)

    with st.spinner("Generating answer from context..."):
        answer = generate_answer(user_query, context)

    st.write("**Answer:**", answer)
