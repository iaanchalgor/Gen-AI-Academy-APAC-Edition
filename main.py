from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class Request(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "AI Agent Running 🚀"}

@app.post("/chat")
def chat(req: Request):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": req.prompt}]
        }
    )
    return response.json()
