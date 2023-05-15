"""The router file for the user"""
from fastapi import APIRouter, status

from schemas.user_schema import UserAuth

from services.user_services import UserService


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.post("/create", name="Create User", description="An endpoint for creating new users for the app", status_code=status.HTTP_201_CREATED)
async def create_user(_data: UserAuth):
    await UserService.create_user(_data)