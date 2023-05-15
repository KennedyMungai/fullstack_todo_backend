"""The file to hold the security logic for the app"""
from typing import Any, Union
from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(_password: str) -> str:
    """Hash the password"""
    return password_context.hash(_password)


def verify_password(_password: str, _hashed_password: str) -> bool:
    """Verify the password"""
    return password_context.verify(_password, _hashed_password)

def create_access_token(_subject: Union[str, Any], expires_delta: int = None) -> str:
    pass