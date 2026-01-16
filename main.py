from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from bot import model

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://shawarmasenpai.vercel.app",  # frontend
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    return {
        "User": data["message"],
        "Shawarma": model(data["message"])
    }


@app.get("/")
def root():
    return {"status": "Shawarma chatbot is running 🚀"}

