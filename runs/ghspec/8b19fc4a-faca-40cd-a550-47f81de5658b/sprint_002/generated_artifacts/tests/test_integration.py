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
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

@pytest.mark.asyncio
async def test_create_student_without_email():
    """Test attempting to create a new student without an email."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/students", json={"name": "Jane Doe"})
        
    # Check if the response is a validation error
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"  # Assumes FastAPI's default message

@pytest.mark.asyncio
async def test_create_student_with_invalid_email():
    """Test attempting to create a new student with an invalid email format."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/students", json={"name": "Invalid Email", "email": "invalidemail"})
        
    # Check if the response is a validation error
    assert response.status_code == 422  # Unprocessable Entity
    assert "value is not a valid email address" in response.json()["detail"][0]["msg"]  # Check specific error message