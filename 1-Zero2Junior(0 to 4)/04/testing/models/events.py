from typing import Optional, List

from beanie import Document
from pydantic import BaseModel


class Event(Document):
    creator: Optional[str]
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Course Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI course in this event.",
                "tags": ["python", "fastapi", "course", "launch"],
                "location": "Google Meet"
            }
        }

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI CourseLaunch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI Course in this event.",
                "tags": ["python", "fastapi", "course", "launch"],
                "location": "Google Meet"
            }
        }
