"""The service file for Todos"""
from models.todo_model import Todo
from models.user_model import User
from typing import List

from schemas.todo_schema import TodoCreate

class TodoService:
    @staticmethod
    async def list_todos(_user: User) -> List[Todo]:
        _todos = await Todo.find(Todo.owner.id == _user.user_id).to_list()
        return _todos
    
    @staticmethod
    async def create_todo(_todo: TodoCreate, _current_user: User) -> Todo:
        _new_todo = Todo(**_todo.dict(), owner=_current_user)
        return await _new_todo.insert()
        