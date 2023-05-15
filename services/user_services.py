"""The file to hold the logic handling the services for the User"""
from typing import Optional

from core.security import hash_password, verify_password
from models.user_model import User
from schemas.user_schema import UserAuth


class UserService:
    """The User Services class"""
    @staticmethod
    async def create_user(_user: UserAuth):
        """The static function that creates a user in the database`

        Args:
            _user (UserAuth): The schema used to create users
        """
        _user_in = User(
            email=_user.email,
            username=_user.username,
            hashed_password=hash_password(_user.password)
        )

        await _user_in.save()

        return _user_in

    @staticmethod
    async def authenticate(_email: str, _password: str) -> Optional[User]:
        """The function to authenticate users

        Args:
            _email (str): The email of the user to be authenticated
            _password (str): The password of the user to be authenticated

        Returns:
            Optional[User]: The authenticated user
        """
        _user = await UserService.get_user_by_email(_email)

        if not _user:
            return None

        if not verify_password(_password, _user.hashed_password):
            return None

        return _user

    @staticmethod
    async def get_user_by_email(_email: str) -> Optional[User]:
        """The function to get a user by email

        Args:
            _email (str): The email of the user to be retrieved

        Returns:
            Optional[User]: The retrieved user
        """
        user = await User.find_one(User.email == _email)
        return user
