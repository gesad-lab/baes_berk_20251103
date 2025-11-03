import pytest
from httpx import AsyncClient
from main import app  # Assuming your FastAPI app is defined in main.py

@pytest.mark.asyncio
async def test_create_student():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/students", json={"name": "John Doe"})
        
    # Check if the response is successful
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}  # Assuming the API returns the created student

@pytest.mark.asyncio
async def test_get_student():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # First create a student to get
        await client.post("/students", json={"name": "Jane Smith"})
        
        # Now, retrieve the student created
        response = await client.get("/students/1")
        
    # Check if the retrieved student is correct
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Jane Smith"}

@pytest.mark.asyncio
async def test_get_student_not_found():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/students/99")  # Assuming this ID does not exist
        
    # Check if the API returns a 404 for a non-existent student
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found", "details": {}}}

@pytest.mark.asyncio
async def test_create_student_invalid_name():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/students", json={"name": ""})  # Invalid empty name
        
    # Check if the API returns a 400 for a validation error
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E400", "message": "Invalid student name", "details": {}}}