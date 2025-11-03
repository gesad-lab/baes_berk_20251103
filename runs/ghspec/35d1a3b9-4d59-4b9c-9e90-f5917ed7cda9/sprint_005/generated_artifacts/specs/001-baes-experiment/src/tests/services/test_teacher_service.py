```python
import pytest
from httpx import AsyncClient
from src.api import app  # Import the FastAPI application
from src.repository import init_db, Teacher  # Ensure Teacher model is available

@pytest.fixture
async def client():
    # This fixture provides a test client for making API requests
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    # Initialize the database for tests
    await init_db()

@pytest.mark.asyncio
async def test_create_teacher(client, setup_database):
    """Test creating a new teacher"""
    response = await client.post(
        "/api/v1/teachers",
        json={
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    )
    
    # Validate response status code
    assert response.status_code == 201
    # Validate response content
    assert response.json() == {
        "message": "Teacher record created successfully",
        "teacher_id": 1  # This value will depend on the actual ID generated in the database
    }

@pytest.mark.asyncio
async def test_get_teacher(client, setup_database):
    """Test retrieving a teacher's information"""
    # Assuming the teacher ID that was created is 1 for the test
    response = await client.get("/api/v1/teachers/1")
    
    # Validate response status code
    assert response.status_code == 200
    # Validate response content structure
    assert "name" in response.json()
    assert "email" in response.json()
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"
```