from fastapi import FastAPI

app = FastAPI(title="User Service")

@app.get("/health")
def health():
    return {"status": "user-service is healthy"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
