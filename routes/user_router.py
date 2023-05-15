"""The router file for the user"""
from fastapi import APIRouter


user_router = APIRouter(prefix="/user", tags=["User"])