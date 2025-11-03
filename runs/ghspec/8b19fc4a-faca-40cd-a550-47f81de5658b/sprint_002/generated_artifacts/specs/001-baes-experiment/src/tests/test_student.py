```python
import pytest
from fastapi import FastAPI
from httpx import AsyncClient

# Import your FastAPI app, replace `my_app` with the correct import
from src.main import app  

@pytest.mark.asyncio
async def test_create_student():
    """Test creating a new student with valid data."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Test case with valid student data including email
        response = await client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
        
    # Check if the response is successful
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

@pytest.mark.asyncio
async def test_create_student_without_email():
    """Test creating a new student without an email should fail."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/students", json={"name": "John Doe"})
        
    # Check if the response is a client error (400 Bad Request)
    assert response.status_code == 400
    assert "email" in response.json()["detail"]["message"]

@pytest.mark.asyncio
async def test_create_student_with_invalid_email():
    """Test creating a new student with an invalid email format should fail."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/students", json={"name": "John Doe", "email": "invalid-email"})
        
    # Check if the response is a client error (400 Bad Request)
    assert response.status_code == 400
    assert "email" in response.json()["detail"]["message"]
```