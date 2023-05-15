"""The router file for the user"""
from fastapi import APIRouter


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get("/", name="User Test Route", description="The route to test the user router")
async def user_test() -> dict[str, str]:
    """The test route for the user router"""
    return {"message": "User Test Route"}