"""The service file for Todos"""
from typing import List
from uuid import UUID

from models.todo_model import Todo
from models.user_model import User
from schemas.todo_schema import TodoCreate, TodoUpdate


class TodoService:
    @staticmethod
    async def list_todos(_user: User) -> List[Todo]:
        _todos = await Todo.find(Todo.owner.id == _user.user_id).to_list()
        return _todos
    
    @staticmethod
    async def create_todo(_todo: TodoCreate, _current_user: User) -> Todo:
        _new_todo = Todo(**_todo.dict(), owner=_current_user)
        return await _new_todo.insert()
    
    @staticmethod
    async def retrieve_todo(_todo_id: UUID, _current_user: User) -> Todo:
        _todo = await Todo.find_one(Todo.owner.id == _current_user.user_id, Todo.id == _todo_id)
        return _todo
    
    @staticmethod
    async def update_todo(_todo_id: UUID, _todo: TodoUpdate, _current_user: User) -> Todo:
        _found_todo = await TodoService.retrieve_todo(_todo_id, _current_user)
        await _found_todo.update({"$set": _todo.dict(exclude_unset=True)})
        
        await _found_todo.save()
        return _found_todo
        
        