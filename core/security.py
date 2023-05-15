"""The file to hold the security logic for the app"""
from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(_password: str) -> str:
    """Hash the password"""
    return password_context.hash(_password)

def verify_password(_password: str, hashed_password: str) -> bool:
    """Verify the password"""
    return password_context.verify(_password, hashed_password)