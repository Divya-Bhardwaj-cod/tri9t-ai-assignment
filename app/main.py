from fastapi import FastAPI

from app.api.document_api import router

app = FastAPI(
    title="Tri9T AI Assignment",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Tri9T AI Backend Running"}