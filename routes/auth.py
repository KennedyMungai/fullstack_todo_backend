"""The file that holds the auth endpoints for the users"""
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from services.user_services import UserService

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/login")
async def login(_form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(_form_data.email, _form_data.password)