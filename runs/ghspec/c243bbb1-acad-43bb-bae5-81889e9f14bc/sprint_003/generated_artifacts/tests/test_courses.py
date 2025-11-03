```python
# tests/test_courses.py

import httpx
import pytest

BASE_URL = "http://localhost:8000/api/v1/courses"

@pytest.mark.asyncio
async def test_create_course_with_valid_data():
    """Test creating a course with valid data."""
    course_data = {
        "name": "Introduction to Python",
        "level": "Beginner"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=course_data)
        
    assert response.status_code == 201
    assert response.json() == {"message": "Course created successfully", "course": course_data}

@pytest.mark.asyncio
async def test_create_course_missing_name():
    """Test creating a course without a name returns an error."""
    course_data = {
        "level": "Beginner"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=course_data)
        
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required.", "details": {}}}

@pytest.mark.asyncio
async def test_create_course_missing_level():
    """Test creating a course without a level returns an error."""
    course_data = {
        "name": "Introduction to Python"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=course_data)
        
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Level is required.", "details": {}}}

@pytest.mark.asyncio
async def test_get_all_courses():
    """Test retrieving all courses returns a list of courses."""
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)
        
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Check that the response is a list
```