"""The file to hold the security logic for the app"""
from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from core.config import settings

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(_password: str) -> str:
    """Hash the password"""
    return password_context.hash(_password)


def verify_password(_password: str, _hashed_password: str) -> bool:
    """Verify the password"""
    return password_context.verify(_password, _hashed_password)


def create_access_token(_subject: Union[str, Any], _expires_delta: int = None) -> str:
    """Function to create access tokens

    Args:
        _subject (Union[str, Any]): The items to be encoded
        _expires_delta (int, optional): The expiration time. Defaults to None.

    Returns:
        str: The access token
    """
    if _expires_delta is not None:
        _expires_delta = datetime.utcnow() + _expires_delta
    else:
        _expires_delta = datetime.utcnow(
        ) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION_MINUTES)

    to_encode = {"exp": _expires_delta, "sub": str(_subject)}

    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)

    return encoded_jwt


def create_refresh_token(_subject: Union[str, Any], _expires_delta: int = None) -> str:
    """Function to create refresh tokens

    Args:
        _subject (Union[str, Any]): The items to be encoded
        _expires_delta (int, optional): The expiration time. Defaults to None.

    Returns:
        str: The access token
    """
    if _expires_delta is not None:
        _expires_delta = datetime.utcnow() + _expires_delta
    else:
        _expires_delta = datetime.utcnow(
        ) + timedelta(minutes=settings.REFRESH_ACCESS_TOKEN_EXPIRATION_MINUTES)

    to_encode = {"exp": _expires_delta, "sub": str(_subject)}

    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_REFRESH_SECRET_KEY, settings.ALGORITHM)

    return encoded_jwt
