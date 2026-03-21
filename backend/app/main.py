from fastapi import FastAPI
import ollama

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate")
def generate(prompt: str):
    # Placeholder for Ollama interaction
    # In a real application, you'd want to handle this asynchronously
    try:
        response = ollama.generate(model='llama2', prompt=prompt)
        return response
    except Exception as e:
        return {"error": str(e)}

