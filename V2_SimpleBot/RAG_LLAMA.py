from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

# 1. DEFINE TOOLS
@tool
def check_order_status(order_id: str):
    """Fetches the live status of an order. Use for order/shipping questions."""
    # Mock logic
    return f"Order {order_id} is currently: SHIPPED."

tools = [check_order_status]

# 2. SETUP MODEL
model = ChatOllama(model="llama3.2", temperature=0)

# 3. DEFINE SYSTEM INSTRUCTIONS (Replaces your old Template)
# No need for {agent_scratchpad} or {input} placeholders!
instructions = (
    "You are a helpful company assistant. "
    "Use 'check_order_status' for customer data."
)

# 4. CREATE THE AGENT
# 'prompt' here serves as the persistent system context
app = create_agent(model, tools, prompt=instructions)

# 5. CHAT LOOP WITH HUMAN MESSAGES
print("🤖 LangGraph Ready!")
while True:
    user_text = input("\nYou: ")
    if user_text.lower() in ["quit", "exit"]: break

    # We wrap the text in a HumanMessage object for maximum control
    inputs = {"messages": [HumanMessage(content=user_text)]}

    try:
        # LangGraph runs the loop (Think -> Act -> Observe)
        result = app.invoke(inputs)

        # The final message in the state is the bot's response
        bot_response = result["messages"][-1].content
        print(f"Bot: {bot_response}")
    except Exception as e:
        print(f"Error: {e}")