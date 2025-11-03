```python
import pytest
from httpx import AsyncClient
from src.api import app  # Import the FastAPI application
from src.repository import init_db, Course  # Import the Course model

@pytest.fixture
async def client():
    # This fixture provides a test client for making API requests
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    # Setup the database before running the tests
    await init_db()  # Assuming this initializes the database
    # Optional: Create any necessary initial data for testing

@pytest.mark.asyncio
async def test_create_course(client):
    # Test creating a new course
    response = await client.post("/courses/", json={"name": "Introduction to Programming", "level": "Beginner"})
    
    assert response.status_code == 201  # Check for successful creation
    assert response.json() == {
        "name": "Introduction to Programming",
        "level": "Beginner"
    }

@pytest.mark.asyncio
async def test_create_course_no_name(client):
    # Test creating a course with no name
    response = await client.post("/courses/", json={"name": "", "level": "Beginner"})
    
    assert response.status_code == 422  # Check for unprocessable entity due to validation
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "name"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

@pytest.mark.asyncio
async def test_create_course_no_level(client):
    # Test creating a course with no level
    response = await client.post("/courses/", json={"name": "Intro to AI", "level": ""})
    
    assert response.status_code == 422  # Check for unprocessable entity due to validation
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "level"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

@pytest.mark.asyncio
async def test_get_courses(client):
    # Test retrieving multiple courses
    response = await client.get("/courses/")
    
    assert response.status_code == 200  # Check for successful retrieval
    assert isinstance(response.json(), list)  # Check response is a list
    # Additional assertions can be done to check for expected course details in the returned list
```