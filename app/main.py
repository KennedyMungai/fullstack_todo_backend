"""The main file for the project"""
from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings


app = FastAPI(
    title="Todo Backend",
    description="The backend of a comprehensive todo application"
)


@app.on_event("startup")
async def startup_event():
    """Logic to run at app startup"""
    print("Connecting to the database")
    db_client = AsyncIOMotorClient(settings.MONGODB_CONN_STRING).todolist
    await init_beanie(db_client, document_models=[])
    print("Connected to the database")


@app.get("/", name="root", description="The root endpoint", tags=["Root"])
async def root() -> dict[str, str]:
    """The root endpoint"""
    return {"message": "The API works"}
