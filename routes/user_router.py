"""The router file for the user"""
from fastapi import APIRouter, HTTPException, status
from pymongo.errors import DuplicateKeyError

from schemas.user_schema import UserAuth
from services.user_services import UserService

user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.post(
    "/create",
    name="Create User",
    description="An endpoint for creating new users for the app",
    status_code=status.HTTP_201_CREATED,
    response_model=UserAuth
)
async def create_user(_data: UserAuth):
    """The endpoint for creating users

    Args:
        _data (UserAuth): The data used to create the user
    """
    try:
        return await UserService.create_user(_data)
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
