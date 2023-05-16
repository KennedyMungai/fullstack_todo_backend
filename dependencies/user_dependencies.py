"""The file which holds the user dependencies"""
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from models.user_model import User
from jose import jwt
from core.config import settings


reusable_oauth = OAuth2PasswordBearer(tokenUrl='/auth/login', scheme_name='JWT')


async def get_current_user(token: str = Depends(reusable_oauth)) -> User:
    try: 
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        token_data = Token()