"""The file that holds the auth endpoints for the users"""
from typing import Any

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from services.user_services import UserService
from fastapi import HTTPException

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/login")
async def login(_form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    _user = await UserService.authenticate(_form_data.email, _form_data.password)
    
    if not _user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Incorrect email or password"
            )
    
    # Create access and refresh tokens
    return