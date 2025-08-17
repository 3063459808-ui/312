import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

# This fixture tells pytest-asyncio to use the asyncio backend for anyio
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

# This fixture creates an instance of the httpx.AsyncClient for testing
# The scope is 'session' so it's created only once for the entire test session
@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
