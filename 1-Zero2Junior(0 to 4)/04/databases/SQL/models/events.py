from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional
from pydantic import BaseModel, ConfigDict


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: list[str] = Field(sa_column=Column(JSON))
    location: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "FastAPI Course Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will talk about FastAPI Course on CodingCogs website!",
                "tags": ["python", "fastapi", "course", "launch"],
                "location": "Google Meet",
            }
        },
    )

class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[list[str]]
    location: Optional[str]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "FastAPI Course Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will talk about FastAPI Course on CodingCogs website!",
                "tags": ["python", "fastapi", "course", "launch"],
                "location": "Google Meet",
            }
        },
    )