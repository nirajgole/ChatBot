from langchain.messages import HumanMessage
from langchain_core.messages import ChatMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3")

messages = [
    ChatMessage(role="control", content="thinking"),
    HumanMessage("What is 3^3?"),
]

response = llm.invoke(messages)
print(response.content)