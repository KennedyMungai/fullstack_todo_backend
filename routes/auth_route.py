"""The file that holds the auth endpoints for the users"""
from datetime import datetime
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import ValidationError

from core.config import settings
from core.security import create_access_token, create_refresh_token
from dependencies.user_dependencies import get_current_user
from models.user_model import User
from schemas.auth_schema import TokenPayload, TokenSchema
from schemas.user_schema import UserOut
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


@auth_router.post(
    "/test-token",
    name="Test Token",
    status_code=status.HTTP_200_OK,
    description="An endpoint to test if the access token is valid", response_model=UserOut
)
async def test_token(_user: User = Depends(get_current_user)) -> Any:
    """The test token endpoint

    Args:
        _user (User, optional): The user that is logged in. Defaults to Depends(get_current_user).

    Returns:
        Any: Any data type can be returned
    """
    return _user


@auth_router.post(
    "/refresh-token",
    name="Refresh Token",
    status_code=status.HTTP_200_OK,
    response_model=TokenSchema
)
async def refresh_access_token(_refresh_token: str = Body(...)) -> TokenSchema:
    """Endpoint renews the access token for the application

    Args:
        _refresh_token (str, optional): The refresh access token. Defaults to Body(...).

    Raises:
        HTTPException: A 401 unauthorized is raised if the access token expires
        HTTPException: A 403 forbidden is raised if the refresh token is invalid
        HTTPException: A 404 not found is raised if the user is not found

    Returns:
        TokenSchema: The new access token
    """
    try:
        payload = jwt.decode(_refresh_token, settings.JWT_SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token expired',
                headers={'WWW-Authenticate': 'Bearer'}
            )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    _user = await UserService.get_user_by_id(token_data.sub)

    if not _user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user"
        )

    return _user
