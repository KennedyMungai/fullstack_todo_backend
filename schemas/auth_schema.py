"""The file which will contain auth schemas for the app"""
from uuid import UUID

from pydantic import BaseModel


class TokenSchema(BaseModel):
    """The schema for the token"""
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    """The Token payload schema"""
    sub: UUID = None
    exp: int = None
