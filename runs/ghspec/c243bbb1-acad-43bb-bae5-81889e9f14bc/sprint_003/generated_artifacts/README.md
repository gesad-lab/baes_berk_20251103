```python
# tests/test_courses.py

import httpx
import pytest

# Define the base URL for the Course API endpoints
BASE_URL = "http://localhost:8000/api/v1/courses"

@pytest.mark.asyncio
async def test_create_course_with_valid_data():
    """Test creating a course with valid data."""
    course_data = {
        "name": "Introduction to Programming",
        "level": "Beginner"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=course_data)
        
    assert response.status_code == 201  # Ensure a course is created
    assert response.json()["name"] == course_data["name"]  # Validate course name
    assert response.json()["level"] == course_data["level"]  # Validate course level

@pytest.mark.asyncio
async def test_create_course_without_name():
    """Test creating a course without a name returns a validation error."""
    course_data = {
        "level": "Beginner"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=course_data)

    assert response.status_code == 400  # Ensure a bad request is returned
    assert response.json()["error"]["code"] == "E001"  # Check for the correct error code
    assert "name is required" in response.json()["error"]["message"]  # Validate error message

@pytest.mark.asyncio
async def test_create_course_without_level():
    """Test creating a course without a level returns a validation error."""
    course_data = {
        "name": "Introduction to Programming"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=course_data)

    assert response.status_code == 400  # Ensure a bad request is returned
    assert response.json()["error"]["code"] == "E001"  # Check for the correct error code
    assert "level is required" in response.json()["error"]["message"]  # Validate error message

@pytest.mark.asyncio
async def test_create_course_with_invalid_level():
    """Test creating a course with invalid level returns a validation error."""
    course_data = {
        "name": "Advanced Topics",
        "level": "UnknownLevel"  # Invalid level
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=course_data)

    assert response.status_code == 400  # Ensure a bad request is returned
    assert response.json()["error"]["code"] == "E002"  # Check for the correct error code
    assert "Invalid course level" in response.json()["error"]["message"]  # Validate error message
```