from fastapi import FastAPI
from Generator_engine import generate_response

app = FastAPI()

@app.get("/")
def root():
    return {"Hello ": "World"}

@app.post("/generate_response")
def generate_chat(prompt: str):
    response = generate_response(prompt)
    return {"response": response}