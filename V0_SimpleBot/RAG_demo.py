from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from ollama import chat
import streamlit as st


# Model: gemma3:latest
# Embedding: embeddinggemma

# Model: llama3.2:latest
# Embedding: llama3.2-embeddings


# load the document
# This will attempt to load ALL files in the directory using the UnstructuredFileLoader
loader = DirectoryLoader(
    "../data/",  # Path to your data directory
    glob="**/*",  # Load all files in the data directory and subdirectories
    loader_cls=UnstructuredFileLoader,
    silent_errors=True,  # Recommended for mixed file types
)
docs = loader.load()

print(f"Loaded {len(docs)} documents.")

# split the document into chunks
# chunk_size should be greater than chunk_overlap
splitter = RecursiveCharacterTextSplitter(chunk_size=2560, chunk_overlap=256)
chunks = splitter.split_documents(docs)

# create the embedding model
embedding_model = OllamaEmbeddings(model="embeddinggemma")
vector_store = Chroma.from_documents(
    chunks, embedding_model, persist_directory="chroma_db"
)


# retrieve the most relevant chunks from the vector store
def retrieve(query: str) -> str:
    return vector_store.similarity_search(query, k=5)


def generate_answer(query: str, context: str) -> str:
    response = chat(
        model="gemma3:latest",
        messages=[
            {
                "role": "user",
                "content": f"Answer the questions based on the provided context.\n\nContext:{context}",
            },
            {
                "role": "user",
                "content": query,
            },
        ],
    )
    return response["message"]["content"]


st.title("PDF RAG with Ollama 🦙 and Chroma")
st.subheader("Ask questions about your documents! 📄")
user_query = st.text_input("Enter your question:")

if user_query:
    with st.spinner("Generating answer..."):
        cxt = retrieve(user_query)

    with st.spinner("Generating answer from context..."):
        answer = generate_answer(user_query, cxt)

    st.write("**Answer:**", answer)
