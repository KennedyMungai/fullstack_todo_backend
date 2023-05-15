"""The file that contains the user schemas"""
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    """The User Auth schema

    Args:
        BaseModel (Pydantic): The parent class for the UserAuth schema
    """
    email: EmailStr = Field(..., description="The user email")
    username: str = Field(..., min_length=3, max_length=400,
                          description="The user username")
    password: str = Field(..., min_length=5, max_length=24,
                          description="The user password")


class UserOut(BaseModel):
    user_id: UUID
    username: str
    email:EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: bool = False