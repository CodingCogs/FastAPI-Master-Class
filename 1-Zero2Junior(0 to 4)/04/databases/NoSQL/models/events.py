from beanie import Document
from typing import Optional
from pydantic import BaseModel, ConfigDict

class Event(Document):
    title: str
    image: str
    description: str
    tags: list[str]
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
    class Settings:
        name = "events"

class EventUpdate(BaseModel):
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