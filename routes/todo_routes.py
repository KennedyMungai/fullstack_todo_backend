"""The file tha holds the Todo endpoints"""
from typing import List

from fastapi import APIRouter, Depends

from dependencies.user_dependencies import get_current_user
from models.user_model import User
from schemas.todo_schema import TodoOut

todo_router = APIRouter(prefix="/todo", tags=["Todo"])


@todo_router.get(
    "/test-todo",
    name="Test Todo router",
    description="An endpoint to test the Todo router",
    response_model=dict
)
async def test_todo_router():
    """Test Todo router"""
    return {"Todo Router": "Works"}


@todo_router.get(
    "/", 
    name="Retrieve all Todos", 
    description="An endpoint to retrieve all Todos", 
    response_model=List[TodoOut]
    )
async def get_all_todos(_current_user: User = Depends(get_current_user)):
    pass