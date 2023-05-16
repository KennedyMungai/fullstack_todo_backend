"""The file tha holds the Todo endpoints"""
from fastapi import APIRouter, Depends


todo_router = APIRouter(prefix="/todo", tags=["Todo"])


@todo_router.get(
    "/", 
    name="Test Todo router", 
    description="An endpoint to test the Todo router",  
    response_model=dict
    )
async def test_todo_router():
    """Test Todo router"""
    return {"Todo Router": "Works"}