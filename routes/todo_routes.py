"""The file tha holds the Todo endpoints"""
from typing import List

from fastapi import APIRouter, Depends, status

from dependencies.user_dependencies import get_current_user
from models.todo_model import Todo
from models.user_model import User
from schemas.todo_schema import TodoCreate, TodoOut
from services.todo_service import TodoService

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
    return await TodoService.list_todos(_current_user)


@todo_router.post(
    "/create", 
    name="Create Todo", 
    description="An endpoint to create a Todo", 
    response_model=Todo,
    status_code=status.HTTP_201_CREATED
    )
async def create_todo_endpoint(_todo: TodoCreate, _current_user: User = Depends(get_current_user)):
    return await TodoService.create_todo(_todo, _current_user)