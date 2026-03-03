from fastapi import FastAPI

app = FastAPI(title="Auth Service")

@app.get("/health")
def health():
    print('auth-service is healthy')
    return {"status": "auth-service is healthy"}

@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "admin":
        return {"token": "fake-jwt-token"}
    return {"error": "invalid credentials"}
