"""The main file for the project"""
from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


app = FastAPI(
    title="Todo Backend",
    description="The backend of a comprehensive todo application"
)


@app.get("/", name="root", description="The root endpoint", tags=["Root"])
async def root() -> dict[str, str]:
    """The root endpoint"""
    return {"message": "The API works"}
