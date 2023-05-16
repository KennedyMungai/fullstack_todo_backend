"""Created a Todo schema file"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    """The schema used when creating todos

    Args:
        BaseModel (Pydantic): The base class for all schemas
    """
    title: str = Field(..., title="Title", max_length=55, min_length=1, description="Title of the todo")
    description: str = Field(..., title="Description", max_length=1000, min_length=1, description="Description of the todo")
    status: Optional[bool] = False
    
    
class TodoUpdate(BaseModel):
    """The schema used when updating todos

    Args:
        BaseModel (Pydantic): The parent class for all schemas
    """
    title: Optional[str] = Field(None, title="Title", max_length=55, min_length=1, description="Title of the todo")
    description: Optional[str] = Field(None, title="Description", max_length=1000, min_length=1, description="Description of the todo")
    status: Optional[bool] = False


class TodoOut(BaseModel):
    """The schema used when returning todos

    Args:
        BaseModel (Pydantic): The parent class for all schemas
    """
    todo_id: UUID
    status: bool
    title: str
    description: str
    created_at: datetime
    updated_at: datetime