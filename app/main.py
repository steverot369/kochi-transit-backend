from fastapi import FastAPI
from app.api.stops import router as stop_router

app = FastAPI(
    title="Kochi Transit API"
)

@app.get("/")
def home():
    return {
        "message": "Kochi Transit Running"
    }
app.include_router(

    stop_router,

    prefix="/api",

    tags=["Stops"]

)