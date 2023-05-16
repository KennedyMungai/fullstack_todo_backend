"""The file which holds the user dependencies"""
from datetime import datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import ValidationError

from core.config import settings
from models.user_model import User
from schemas.auth_schema import TokenPayload
from services.user_services import UserService


reusable_oauth = OAuth2PasswordBearer(
    tokenUrl='/auth/login', scheme_name='JWT')


async def get_current_user(token: str = Depends(reusable_oauth)) -> User:
    """A  function to get details of the currently logged in user

    Args:
        token (str, optional): The token created by the login endpoint. Defaults to Depends(reusable_oauth).

    Raises:
        HTTPException: A 401 forbidden unauthorized is raised when the access token expired
        HTTPException: A 403 unauthorized is raised when the access token is invalid

    Returns:
        User: The details of the currently logged in user
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY,
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

    user = await User()