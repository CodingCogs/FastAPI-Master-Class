from beanie import Document
from typing import Optional
from models.events import Event
from pydantic import BaseModel, EmailStr, ConfigDict


class User(Document):
    email: EmailStr
    password: str
    events: Optional[list[Event]]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "fastapi@codingcogs.org",
                "password": "strong!!!",
                "events": [],
            }
        },
    )
    
    class Settings:
        name = "users"


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {"email": "fastapi@codingcogs.org", "password": "strong!!!"}
        },
    )


class NewUser(UserSignIn):
    pass
