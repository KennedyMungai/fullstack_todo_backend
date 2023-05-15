"""The file that holds the auth endpoints for the users"""
from fastapi import APIRouter


auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/login")
async def login():
    pass