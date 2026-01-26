import requests

API_BASE_URL = "http://localhost:8001"

def fetch_order_status(order_id: str):
    response = requests.get(
        f"{API_BASE_URL}/order/status",
        params={"order_id": order_id}
    )
    return response.json()
