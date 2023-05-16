"""The file which holds the user dependencies"""
from datetime import datetime
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from models.user_model import User
from jose import jwt, JWTError
from core.config import settings
from schemas.auth_schema import TokenPayload
from fastapi import HTTPException


reusable_oauth = OAuth2PasswordBearer(
    tokenUrl='/auth/login', scheme_name='JWT')


async def get_current_user(token: str = Depends(reusable_oauth)) -> User:
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
