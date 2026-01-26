from api_client import (
    fetch_order_status,
    cancel_order,
    create_ticket,
    fetch_account_balance,
)

ROUTES = {
    "order_status": fetch_order_status,
    "cancel_order": cancel_order,
    "create_ticket": create_ticket,
    "account_balance": fetch_account_balance,
}
