from intent_chain import intent_chain
from intent_validator import validate_intent
from router import ROUTES
from response_chain import response_chain

def chatbot():
    print("🤖 Bot: How can I help you?")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        try:
            intent_data = intent_chain.invoke({"input": user_input})
        except:
            print("🤖 Bot: I didn't understand that.")
            continue

        is_valid, result = validate_intent(intent_data)

        if not is_valid:
            if result.startswith("missing_fields"):
                print("🤖 Bot: I need more information to help you.")
            else:
                print("🤖 Bot: Sorry, I can’t help with that yet.")
            continue

        handler = ROUTES[result]
        api_response = handler(**intent_data["fields"])

        response = response_chain.invoke({
            "order_data": api_response
        })

        print("🤖 Bot:", response.content)
