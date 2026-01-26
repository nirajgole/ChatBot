from fastapi import FastAPI
import uvicorn

app = FastAPI(title="HR", version="1.0", description="HR server!")

@app.get("/order/status")
def get_order_status(order_id: str):
    return {
        "order_id": order_id,
        "status": "shipped",
        "delivery_date": "2026-02-01"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)