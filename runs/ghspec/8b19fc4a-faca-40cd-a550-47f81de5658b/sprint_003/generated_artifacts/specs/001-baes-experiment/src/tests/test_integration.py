```python
import pytest
from httpx import AsyncClient
from main import app  # Assuming your FastAPI app is defined in main.py

@pytest.mark.asyncio
async def test_create_student_with_email():
    """Test creating a new student with valid email."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    
    # Check if the response is successful
    assert response.status_code == 201

@pytest.mark.asyncio
async def test_create_course():
    """Test creating a new course with valid data."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/courses", json={"name": "Python Programming", "level": "Beginner"})
    
    assert response.status_code == 201
    assert response.json()["name"] == "Python Programming"
    assert response.json()["level"] == "Beginner"

@pytest.mark.asyncio
async def test_create_course_missing_fields():
    """Test creating a course without required fields."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/courses", json={"name": ""})
    
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"

@pytest.mark.asyncio
async def test_get_course():
    """Test retrieving a specific course by ID."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # First, we need to create a course to retrieve it
        create_response = await client.post("/courses", json={"name": "JavaScript Basics", "level": "Intermediate"})
        course_id = create_response.json()["id"]

        # Now retrieve the course using the ID
        response = await client.get(f"/courses/{course_id}")

    assert response.status_code == 200
    assert response.json()["id"] == course_id
    assert response.json()["name"] == "JavaScript Basics"
    assert response.json()["level"] == "Intermediate"
```