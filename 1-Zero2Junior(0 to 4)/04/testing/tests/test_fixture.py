import pytest

# Fixture is defined.
from models.events import EventUpdate


@pytest.fixture
def event() -> EventUpdate:
    return EventUpdate(
        title="FastAPI Course Launch",
        image="https://codigncogs.com/fastapi.png",
        description="We will be discussing the contents of the FastAPI Course in this event.",
        tags=["python", "fastapi", "course", "launch"],
        location="Google Meet"
    )


def test_event_name(event: EventUpdate) -> None:
    assert event.title == "FastAPI Course Launch"
