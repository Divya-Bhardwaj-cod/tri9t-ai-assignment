from fastapi import FastAPI

app = FastAPI(
    title="Tri9T AI Assignment",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Tri9T AI Backend Running"
    }