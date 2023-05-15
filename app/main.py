"""The main file for the project"""
from fastapi import FastAPI


app = FastAPI(
    title="Todo Backend", 
    description="The backend of a comprehensive todo application"
    )


@app.get("/", name="root", description="The root endpoint", tags=["Root"])
async def root() -> dict[str, str]:
    return {"message": "The API works"}