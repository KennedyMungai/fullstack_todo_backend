"""The router file for the user"""
from fastapi import APIRouter

from schemas.user_schema import UserAuth


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.post("/create", name="Create User", description="An endpoint for creating new users for the app")
async def create_user(data: UserAuth):
    return {"message": "Create User endpoint"}