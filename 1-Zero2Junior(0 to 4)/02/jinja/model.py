from typing import List, Optional  # new
from pydantic import BaseModel


class Todo(BaseModel):
    id: Optional[int]
    item: str

    # new
    @classmethod
    def as_form(cls, item: str = Form(...), id: Optional[int] = None):
        return cls(item=item, id=id)

    class Config:
        pass
