```python
import pytest
from httpx import AsyncClient
from src.main import app  # Assuming the FastAPI app is instantiated in main.py
from src.database import init_db, get_db  # Function to initialize and access the database
from src.models import Course  # The Course model should be defined appropriately to match the database schema

@pytest.fixture(scope="module")
async def test_client():
    # Initialize the database before the tests and create the necessary tables
    await init_db()
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client  # This will provide a test client for the tests

@pytest.mark.asyncio
async def test_create_course(test_client):
    # Test creating a new course
    course_data = {"name": "Mathematics", "level": "100"}
    response = await test_client.post("/courses/", json=course_data)
    
    assert response.status_code == 201  # Check for success
    assert response.json() == {"id": response.json()['id'], "name": "Mathematics", "level": "100"}

@pytest.mark.asyncio
async def test_retrieve_courses(test_client):
    # Test retrieving all courses
    response = await test_client.get("/courses/")
    
    assert response.status_code == 200  # Check for success
    assert isinstance(response.json(), list)  # Ensure the response is a list

@pytest.mark.asyncio
async def test_create_course_missing_fields(test_client):
    # Test creating a course with missing fields
    course_data = {"name": "", "level": ""}
    response = await test_client.post("/courses/", json=course_data)
    
    assert response.status_code == 400  # Check for client error
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Both name and level fields are required.",
            "details": {}
        }
    }

@pytest.mark.asyncio
async def test_create_course_invalid_level(test_client):
    # Test creating a course with an invalid level format
    course_data = {"name": "Biology", "level": "InvalidLevel"}
    response = await test_client.post("/courses/", json=course_data)
    
    assert response.status_code == 400  # Check for client error
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Level format is invalid.",
            "details": {}
        }
    }
```