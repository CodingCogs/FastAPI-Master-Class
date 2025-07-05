import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_sign_new_user(client: AsyncClient) -> None:
    payload = {
        'email': 'testuser@codingcogs.org',
        'password': 'testpassword',
        "events": [],
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    test_response = {
        "message": "User successfully registered!"
    }
    response = await client.post('/user/signup', json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response
    
@pytest.mark.asyncio
async def test_sign_user_in(client: AsyncClient) -> None:
    payload = {
        "username": "testuser@codingcogs.org",
        "password": "testpassword"
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = await client.post("/user/signin", data=payload, headers=headers)

    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"