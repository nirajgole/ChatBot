INTENT_REGISTRY = {
    "order_status": {
        "description": "Check status of an order",
        "required_fields": ["order_id"]
    },
    "cancel_order": {
        "description": "Cancel an existing order",
        "required_fields": ["order_id"]
    },
    "create_ticket": {
        "description": "Create a support ticket",
        "required_fields": ["issue"]
    },
    "account_balance": {
        "description": "Get account balance",
        "required_fields": ["user_id"]
    },
    # ... add up to 20+
}
