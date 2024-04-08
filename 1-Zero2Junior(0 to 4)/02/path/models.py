from pydantic import BaseModel
from models import Todo


class Todo(BaseMode):
    id: int
    item: str
