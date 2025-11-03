```python
# tests/test_courses_api.py

import httpx
import pytest

BASE_URL = "http://localhost:8000/api/v1/courses"

@pytest.mark.asyncio
async def test_create_course_with_valid_data():
    """Test creating a course with valid data."""
    course_data = {
        "name": "Mathematics",
        "level": "Introductory"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=course_data)

    assert response.status_code == 201  # Expecting a 201 Created status
    assert response.json() == {"message": "Course created successfully"}

@pytest.mark.asyncio
async def test_retrieve_all_courses():
    """Test retrieving all courses."""
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)

    assert response.status_code == 200  # Expecting a 200 OK status
    assert isinstance(response.json(), list)  # Expecting a list of courses

@pytest.mark.asyncio
async def test_create_course_without_name():
    """Test creating a course without a name."""
    course_data = {
        "level": "Intermediate"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=course_data)

    assert response.status_code == 400  # Expecting a 400 Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required",
            "details": {}
        }
    }

@pytest.mark.asyncio
async def test_create_course_without_level():
    """Test creating a course without a level."""
    course_data = {
        "name": "History"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=course_data)

    assert response.status_code == 400  # Expecting a 400 Bad Request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Level is required",
            "details": {}
        }
    }

```