from fastapi import APIRouter, Path, HTTPException, status
from models import Todo, TodoItem,TodoItems

todo_router = APIRouter()

todo_list = []

@todo_router.post('/todo',status_code=201)
async def add_todo(todo:Todo) -> dict:
    todo_list.append(todo)
    return {'message':"Todo added successfully"}

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {'todos': todo_list}



@todo_router.get("/todo/{todo_id}")
async def retrieve_todo(todo_id: int = Path(...,title="The ID of the todo to retrieve", description="ID of the TODO")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    # return {'message': "ID doesn't exist"}
    # new
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail = "Todo with supplied ID doesn't exist",
    )

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(...,title="The ID of the todo to update", description="ID of the TODO")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully."}
    return {'message': "ID doesn't exist"}

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int = Path(...,title="The ID of the todo to Delete", description="ID of the TODO")) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }