import pytest
from httpx import AsyncClient
from auth.jwt_handler import create_access_token
from models.events import Event

@pytest.fixture(scope="session")
async def access_token() -> str:
    return create_access_token("testuser@codingcogs.org")

@pytest.fixture(scope="function")
async def mock_event() -> Event:
    new_event = Event(
        creator="testuser@codingcogs.org",
        title="FastAPI Course Launch",
        image="https://codingcogs.org/fastapi.png",
        description="We will talk about FastAPI Course on CodingCogs website!",
        tags=["python", "fastapi", "course", "launch"],
        location="Google Meet",
        
    )

    await Event.insert_one(new_event)

    yield new_event

@pytest.mark.asyncio
async def test_get_events(client: AsyncClient, mock_event: Event) -> None:
    response = await client.get('/event/')
    assert response.status_code == 200
    assert response.json()[0]['_id'] == str(mock_event.id)
    
@pytest.mark.asyncio
async def test_get_event(client: AsyncClient, mock_event: Event) -> None:
    url = f"/event/{str(mock_event.id)}"
    response = await client.get(url)

    assert response.status_code == 200
    assert response.json()["creator"] == mock_event.creator
    assert response.json()["_id"] == str(mock_event.id)
    
@pytest.mark.asyncio
async def test_post_event(client: AsyncClient, access_token: str) -> None:
    payload = {
        "title": "FastAPI Course Launch",
        "image": "https://linktomyimage.com/image.png",
        "description": "We will talk about FastAPI Course on CodingCogs website!",
        "tags": ["python", "fastapi", "course", "launch"],
        "location": "Google Meet",
        "creator": "",
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    test_response = {
        "message": "Event created successfully"
    }

    response = await client.post("/event/new", json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json() == test_response
    
@pytest.mark.asyncio
async def test_update_event(client: AsyncClient, mock_event: Event, access_token: str) -> None:
    test_payload = {
        "title": "Updated FastAPI event"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    url = f"/event/edit/{str(mock_event.id)}"

    response = await client.put(url, json=test_payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["title"] == test_payload["title"]
    
@pytest.mark.asyncio
async def test_delete_event(client: AsyncClient, mock_event: Event, access_token: str) -> None:
    test_response = {
        "message": "Event deleted successfully"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    url = f"/event/{mock_event.id}"

    response = await client.delete(url, headers=headers)

    assert response.status_code == 200
    assert response.json() == test_response