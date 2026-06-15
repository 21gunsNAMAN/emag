from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Railway deployment successful, congratulations Naman bhai..."
    }