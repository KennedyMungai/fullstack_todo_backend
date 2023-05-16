"""The service file for Todos"""
from models.todo_model import Todo
from models.user_model import User

class TodoService:
    @staticmethod
    async def list_todos(_user: User):
        pass