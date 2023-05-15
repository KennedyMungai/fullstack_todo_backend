"""The file that contains the user schemas"""
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="The user email")
    username: str = Field(..., min_length=3, max_length=400, description="The user username")
    password: str = Field(..., min_length=5, max_length=24, description="The user password")