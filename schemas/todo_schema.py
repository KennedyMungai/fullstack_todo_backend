"""Created a Todo schema file"""
from pydantic import BaseModel, Field
from typing import Optional


class TodoCreate(BaseModel):
    title: str = Field(..., title="Title", max_length=55, min_length=1, description="Title of the todo")
    description: str = Field(..., title="Description", max_length=1000, min_length=1, description="Description of the todo")
    status: Optional[bool] = False
    
    
class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, title="Title", max_length=55, min_length=1, description="Title of the todo")
    description: Optional[str] = Field(None, title="Description", max_length=1000, min_length=1, description="Description of the todo")
    status: Optional[bool] = False
