from fastapi import APIRouter, Path, HTTPException, status, Request, Depends  # new
from fastapi.templating import Jinja2Templates  # new
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []
templates = Jinja2Templates(directory="templates/")  # new


# new
@todo_router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse(
        "todo.html", {"request": request, "todos": todo_list}
    )
