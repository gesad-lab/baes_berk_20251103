```python
import pytest
from fastapi import FastAPI
from httpx import AsyncClient

# Import your FastAPI app, replace `my_app` with the correct import
from src.main import app  

@pytest.mark.asyncio
async def test_create_course():
    """Test creating a new course with valid data."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Test case with valid course data
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
    assert response.json()["error"]["message"] == "Both name and level fields are required."

@pytest.mark.asyncio
async def test_retrieve_course_information():
    """Test retrieving information about a specific course."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # First, create the course to retrieve later
        await client.post("/courses", json={"name": "Python Programming", "level": "Beginner"})
        
        # Now retrieve the course information
        response = await client.get("/courses/1")
    
    assert response.status_code == 200
    assert response.json()["name"] == "Python Programming"
    assert response.json()["level"] == "Beginner"
```