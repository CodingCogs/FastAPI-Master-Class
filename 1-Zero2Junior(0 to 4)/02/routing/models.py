from pydantic import BaseModel
from models import Todo


class Todo(BaseModel):
    id: int
    item: str
