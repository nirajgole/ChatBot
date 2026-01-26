from intents import INTENT_REGISTRY

def validate_intent(intent_data: dict):
    intent = intent_data.get("intent")

    if intent not in INTENT_REGISTRY:
        return False, "unknown"

    required = INTENT_REGISTRY[intent]["required_fields"]
    fields = intent_data.get("fields", {})

    missing = [f for f in required if f not in fields]

    if missing:
        return False, f"missing_fields:{missing}"

    return True, intent
