"""The main file for the project"""
from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings
from models.todo_model import Todo
from models.user_model import User
from routes.auth_route import auth_router
from routes.todo_routes import todo_router
from routes.user_router import user_router

app = FastAPI(
    title="Todo Backend",
    description="The backend of a comprehensive todo application"
)


@app.on_event("startup")
async def startup_event():
    """Logic to run at app startup"""
    print("Connecting to the database")
    db_client = AsyncIOMotorClient(settings.MONGODB_CONN_STRING).todolist
    await init_beanie(db_client, document_models=[User, Todo])
    print("Connected to the database")


@app.get("/", name="root", description="The root endpoint", tags=["Root"])
async def root() -> dict[str, str]:
    """The root endpoint"""
    return {"message": "The API works"}

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(todo_router)
