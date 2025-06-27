from pydantic import BaseModel, ConfigDict


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "FastAPI Course Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will talk about FastAPI Course on CodingCogs website!",
                "tags": ["python", "fastapi", "course", "launch"],
                "location": "Google Meet",
            }
        },
    )
