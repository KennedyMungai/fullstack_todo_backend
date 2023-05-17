"""The service file for Todos"""
from typing import List
from uuid import UUID

from models.todo_model import Todo
from models.user_model import User
from schemas.todo_schema import TodoCreate, TodoUpdate


class TodoService:
    """The class that holds the services for the Todo routes"""
    @staticmethod
    async def list_todos(_user: User) -> List[Todo]:
        """The service function to retrieve all the todos by a specific user

        Args:
            _user (User): The logged in user

        Returns:
            List[Todo]: The list of todos by the user
        """
        _todos = await Todo.find(Todo.owner.id == _user.user_id).to_list()
        return _todos

    @staticmethod
    async def create_todo(_todo: TodoCreate, _current_user: User) -> Todo:
        """The service function to create todos for a specific user

        Args:
            _todo (TodoCreate): The todo to be created
            _current_user (User): The currently logged in user

        Returns:
            Todo: _description_
        """
        _new_todo = Todo(**_todo.dict(), owner=_current_user)
        return await _new_todo.insert()

    @staticmethod
    async def retrieve_todo(_todo_id: UUID, _current_user: User) -> Todo:
        """The service function to retrieve a todo by id

        Args:
            _todo_id (UUID): The id of the todo
            _current_user (User): The currently logged in user

        Returns:
            Todo: The todo by id
        """
        _todo = await Todo.find_one(Todo.owner.id == _current_user.id, Todo.id == _todo_id)
        return _todo

    @staticmethod
    async def update_todo(_todo_id: UUID, _todo: TodoUpdate, _current_user: User) -> Todo:
        """The service function to update a todo

        Args:
            _todo_id (UUID): The id of the todo
            _todo (TodoUpdate): The template used to update the todo
            _current_user (User): The logged in user

        Returns:
            Todo: The updated todo
        """
        _found_todo = await TodoService.retrieve_todo(_todo_id, _current_user)
        await _found_todo.update({"$set": _todo.dict(exclude_unset=True)})

        await _found_todo.save()
        return _found_todo

    @staticmethod
    async def delete_todo(_todo_id: UUID, _current_user: User) -> None:
        """The service function to delete Todos

        Args:
            _todo_id (UUID): The id of the todo in the database
            _current_user (User): The logged in user
        """
        _found_todo = await TodoService.retrieve_todo(_todo_id, _current_user)

        if not _found_todo:
            return None

        await _found_todo.delete()
