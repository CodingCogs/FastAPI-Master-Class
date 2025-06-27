from pydantic import BaseModel, ConfigDict

class Todo(BaseModel):
    id: int
    item: str
    
    # new
    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "یک"
            }
        }
    )
    
class TodoItem(BaseModel):
    item: str
    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "item": "یک"
            }
        }
    )