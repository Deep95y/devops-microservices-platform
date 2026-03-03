from fastapi import FastAPI

app = FastAPI(title="Order Service")

@app.get("/health")
def health():
    return {"status": "order-service is healthy"}

# @app.post("create-order")
# def create_orders(order_id: int, item: str):
#     return ({
#         "order_id":order_id, "item": item
#     })

@app.get("/orders")
def get_orders():
    return [
        {"order_id": 101, "item": "Laptop"},
        {"order_id": 102, "item": "Phone"}
    ]
