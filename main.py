from fastapi import FastAPI
from Generator_engine import generate_response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://127.0.0.1:3000/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"msg": "Hello Goodbye"}

@app.post("/generate_response")
def generate_chat(prompt: str):
    response = generate_response(prompt)
    return {"response": response}