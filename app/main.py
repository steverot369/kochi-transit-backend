from fastapi import FastAPI

app = FastAPI(
    title="Kochi Transit API"
)

@app.get("/")
def home():
    return {
        "message": "Kochi Transit Running"
    }