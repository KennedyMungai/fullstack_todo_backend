"""Created a Todo schema file"""
from pydantic import BaseModel, Field
from typing import Optional


class TodoCreate(BaseModel):
    title: str = Field(..., title="Title", max_length=55, min_length=1, description="Title of the todo")
    description: str = Field(..., title="Description", max_length=10000, min_length=1, description="Description of the todo")
    status: Optional[bool] = False
