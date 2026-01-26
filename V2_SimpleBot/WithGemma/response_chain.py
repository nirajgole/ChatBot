from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="gemma3", temperature=0.3)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful customer support chatbot.\n"
            "Be clear, short, and friendly.",
        ),
        ("human", "Order data:\n{order_data}\n\nRespond to the user."),
    ]
)

response_chain = prompt | llm
