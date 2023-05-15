"""The file to hold the security logic for the app"""
from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")