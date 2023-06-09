"""The User Models"""
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from beanie import Document, Indexed
from pydantic import EmailStr, Field


class User(Document):
    """The model for the User data

    Args:
        Document (beanie.Document): The parent for the User model
    """
    user_id: UUID = Field(default_factory=uuid4)
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hashed_password: str
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool]

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def create(self) -> datetime:
        """Returns the user creation time

        Returns:
            datetime: The user creation time
        """
        return self.id.generation_time

    @classmethod
    async def by_email(self, email: str) -> "User":
        """A method of finding users by email

        Args:
            email (str): The user email

        Returns:
            User: The user
        """
        return await self.find_one(self.email == email)

    class Settings:
        """The name of the collection"""
        name = "users"
