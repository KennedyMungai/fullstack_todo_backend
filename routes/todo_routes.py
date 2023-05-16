"""The file tha holds the Todo endpoints"""
from fastapi import APIRouter, Depends


todo_router = APIRouter(prefix="/todo", tags=["Todo"])