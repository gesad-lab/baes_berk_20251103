```python
import pytest
from httpx import AsyncClient
from src.main import app  # Assuming the FastAPI app is instantiated in main.py
from src.database import init_db, get_db  # Function to initialize and access the database
from src.models import Course  # Importing the Course model

@pytest.fixture(scope="module")
async def test_client():
    # Initialize the database before the tests and create the necessary tables
    await init_db()

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_create_course(test_client):
    # Test creating a new course
    course_data = {
        "name": "Introduction to Programming",
        "level": "beginner"
    }
    response = await test_client.post("/api/courses", json=course_data)
    assert response.status_code == 201  # Expect a successful creation
    assert response.json()["course"]["name"] == course_data["name"]
    assert response.json()["course"]["level"] == course_data["level"]

@pytest.mark.asyncio
async def test_retrieve_courses(test_client):
    # Test retrieving existing courses
    response = await test_client.get("/api/courses")
    assert response.status_code == 200  # Expect a successful retrieval
    assert isinstance(response.json(), list)  # Should return a list of courses

@pytest.mark.asyncio
async def test_create_course_missing_fields(test_client):
    # Test creating a course with missing fields
    response = await test_client.post("/api/courses", json={})
    assert response.status_code == 400  # Expect a bad request
    assert response.json()["error"]["code"] == "E001"  # Custom error for missing fields
    assert "name" in response.json()["error"]["message"]
    assert "level" in response.json()["error"]["message"]

@pytest.mark.asyncio
async def test_create_course_invalid_level(test_client):
    # Test creating a course with an invalid level format
    course_data = {
        "name": "Advanced Mathematics",
        "level": "expert-level"  # Assuming "expert-level" is an invalid format
    }
    response = await test_client.post("/api/courses", json=course_data)
    assert response.status_code == 400  # Expect a bad request
    assert response.json()["error"]["code"] == "E002"  # Custom error for invalid level format
```