"""The file that holds the auth endpoints for the users"""
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from core.security import create_access_token, create_refresh_token
from schemas.auth_schema import TokenSchema

from services.user_services import UserService

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post(
    "/login",
    name="Login",
    status_code=status.HTTP_200_OK,
    description="Create Access and Refresh tokens",
    response_model=TokenSchema
)
async def login(_form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """The login endpoint

    Args:
        _form_data (OAuth2PasswordRequestForm, optional): 
                    The data a user uses to login. Defaults to Depends().

    Raises:
        HTTPException: A 400 is raised if a user enters bad credentials

    Returns:
        Any: ANy data type cab be returned
    """
    _user = await UserService.authenticate(_form_data.username, _form_data.password)

    if not _user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(_user.user_id),
        "refresh_token": create_refresh_token(_user.user_id)
    }
