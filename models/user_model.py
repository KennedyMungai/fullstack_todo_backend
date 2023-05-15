"""The User Models"""
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
    user_name = Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hashed_password: str
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool]

    class Settings:
        """The name of the collection"""
        name = "users"
