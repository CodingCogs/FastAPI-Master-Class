from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from models.events import Event


class User(BaseModel):
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
