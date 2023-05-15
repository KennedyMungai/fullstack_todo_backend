"""The router file for the user"""
from fastapi import APIRouter


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.post("/create", name="Create User", description="An endpoint for creating new users for the app")
async def create_user(data):
    return {"message": "Create User endpoint"}