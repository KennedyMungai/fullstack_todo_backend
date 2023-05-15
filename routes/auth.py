"""The file that holds the auth endpoints for the users"""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any


auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/login")
async def login(_login: OAuth2PasswordRequestForm = Depends()) -> Any:
    pass