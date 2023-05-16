"""The file to hold the models for the Todos"""
from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field

from models.user_model import User


class Todo(Document):
    """The model for the Todo data

    Args:
        Document (Beanie): The parent class for the Todo model
    """
    todo_id: UUID = Field(default_factory=uuid4, unique=True)
    status: bool = False
    title: Indexed(str)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    def __repr__(self) -> str:
        return f"Todo: {self.title}"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Todo):
            return False
        return self.title == other.title
