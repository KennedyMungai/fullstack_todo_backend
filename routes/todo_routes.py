"""The file tha holds the Todo endpoints"""
from fastapi import APIRouter


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


@todo_router.get("/", name="Retrieve all Todos", description="An endpoint to retrieve all Todos")
async def get_all_todos():
    """Retrieve all Todos"""
    return {"Todos": "Works"}