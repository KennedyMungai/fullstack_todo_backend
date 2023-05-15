"""The file to hold the logic handling the services for the User"""
from schemas.user_schema import UserAuth
from models.user_model import User
from core.security import hash_password


class UserService:
    @staticmethod
    async def create_user(_user: UserAuth):
        _user_in = User(
            email=_user.email,
           username= _user.username,
           hashed_password= _user.password
        )