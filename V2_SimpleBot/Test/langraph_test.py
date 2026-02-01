from typing import Annotated
from dotenv import load_dotenv

load_dotenv()

from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# from langchain_ollama import ChatOllama
# llm = ChatOllama(model="gemma3")

# llm = init_chat_model("llama3.2", model_provider="ollama", temperature=0)
llm = init_chat_model("gemma3", model_provider="ollama", temperature=0)


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State) -> State:
    return {"messages": [llm.invoke(state["messages"])]}


builder = StateGraph(State)
builder.add_node("chatbot_node", chatbot)

builder.add_edge(START, "chatbot_node")
builder.add_edge("chatbot_node", END)

graph = builder.compile()

message = {"role": "user", "content": "Who walked on the moon for the first time? Print only the name"}
# message = {"role": "user", "content": "What is the latest price of MSFT stock?"}
# response = graph.invoke({"messages":[message]})

# response["messages"]

state = None
while True:
    in_message = input("You: ")
    if in_message.lower() in {"quit","exit"}:
        break
    if state is None:
        state: State = {
            "messages": [{"role": "user", "content": in_message}]
        }
    else:
        state["messages"].append({"role": "user", "content": in_message})

    state = graph.invoke(state)
    print("Bot:", state["messages"][-1].content)