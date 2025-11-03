```python
import pytest
from httpx import AsyncClient
from src.api import app  # Import the FastAPI application
from src.repository import init_db, Teacher  # Import the Teacher model
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
async def client():
    # This fixture provides a test client for making API requests
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    # Setup database before tests and teardown after tests
    async with AsyncSession() as session:
        await init_db(session)  # Initialize the database
        yield
        # Drop fixtures here if needed (not shown)


@pytest.mark.asyncio
async def test_create_teacher(client):
    # Test case for creating a new teacher
    response = await client.post(
        "/teachers/",
        json={"name": "John Doe", "email": "john.doe@example.com"},
    )
    
    # Check that the response status is 201 Created
    assert response.status_code == 201
    assert response.json() == {"message": "Teacher created successfully."}

    # Check for the newly created teacher in the database (add actual retrieval logic)


@pytest.mark.asyncio
async def test_retrieve_teacher(client):
    # Assuming we have a teacher created with ID 1
    response = await client.get("/teachers/1/")
    
    # Check that the response status is 200 OK
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }  # Replace with expected data
```