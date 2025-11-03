```python
import pytest
from fastapi import FastAPI
from httpx import AsyncClient

# Import your FastAPI app, replace `my_app` with the correct import
from src.main import app  

@pytest.mark.asyncio
async def test_create_student():
    """Test creating a new student."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}  # Adjust according to your response structure

@pytest.mark.asyncio
async def test_create_student_without_name():
    """Test creating a student without a name should fail."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/students", json={})
    assert response.status_code == 400  # Bad request due to validation error
    assert response.json() == {
        "error": {"code": "E001", "message": "Name is required"}
    }  # Assuming this is your error response structure

@pytest.mark.asyncio
async def test_get_student():
    """Test retrieving student details."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # First create a student to get
        create_response = await client.post("/students", json={"name": "John Doe"})
        student_id = create_response.json()["id"]
        
        # Now get the student
        response = await client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json() == {"id": student_id, "name": "John Doe"}  # Adjust according to your response structure

@pytest.mark.asyncio
async def test_get_student_not_found():
    """Test trying to retrieve a student that does not exist."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/students/99999")  # Assuming 99999 is a non-existing ID
    assert response.status_code == 404  # Not found
    assert response.json() == {
        "error": {"code": "E002", "message": "Student not found"}
    }  # Assuming this is your error response structure
```