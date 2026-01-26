# import requests
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.agents import AgentExecutor
from langchain.agents.tool_calling_agent import create_tool_calling_agent
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate

# --- CONFIGURATION ---
VECTOR_DB_PATH = "./my_local_db"
LLM_MODEL = "llama3.1"  # Must support tool use

# --- STEP 1: DEFINE YOUR API TOOL (The Hands) ---
@tool
def check_order_status(order_id: str):
    """
    Fetches the live status of an order.
    Use this when the user asks about their order, shipping, or delivery.
    """
    print(f"\n[System] Connecting to API for Order #{order_id}...")

    # SIMULATING YOUR API CALL HERE
    # In reality, you would do: response = requests.get(f"https://api.yoursite.com/orders/{order_id}")
    # try:
    #     response = requests.get(f"https://api.yoursite.com/orders/{order_id}")
    # except requests.exceptions.RequestException as e:
    #     return {"error": f"API request failed: {e}"}

    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     return {"error": "Order not found"}
    # # Mock response for testing:
    if order_id == "12345":
        return {"status": "Shipped", "delivery_date": "2023-10-25"}
    else:
        return {"error": "Order not found"}


# --- STEP 2: SETUP KNOWLEDGE RETRIEVAL (The Brain) ---
# embedding_model = OllamaEmbeddings(model="nomic-embed-text")
# vectorstore = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embedding_model)
# retriever = vectorstore.as_retriever()

# from langchain.tools.retriever import create_retriever_tool
# website_search_tool = create_retriever_tool(
#     retriever,
#     "search_website_knowledge",
#     "Searches the company website for static info like policies, hours, and about us."
# )

# Combine all tools
tools = [
    check_order_status,
    # website_search_tool
]

# --- STEP 3: INITIALIZE OLLAMA AGENT ---
model = ChatOllama(model=LLM_MODEL, temperature=0)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant for a company. Use the website search for general questions and the order tool for specific customer data.",
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

from langchain.agents import create_agent


@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    return f"Weather in {location}: Sunny, 72°F"

agent = create_agent(model, tools=[search, get_weather])

# agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# --- STEP 4: RUN THE CHAT LOOP ---
print("🤖 Local Bot Ready! (Type 'quit' to exit)")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["quit", "exit"]:
        break

    try:
        response = agent_executor.invoke({"input": user_input})
        print(f"Bot: {response['output']}")
    except Exception as e:
        print(f"Error: {e}")
