from httpx import AsyncClient
import pytest
from database.connection import Settings
from models.events import Event
from models.users import User
from main import app

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
        await Event.delete_all()
        await User.delete_all()

# Database session fixture
@pytest.fixture(autouse=True)
async def db_session():
    test_settings = Settings()
    test_settings.DATABASE_URL = 'mongodb://username:password@localhost:27017'
    await test_settings.initialize_test_database()