```python
# tests/test_teachers.py

import pytest
from httpx import AsyncClient
from main import app  # Assuming your FastAPI app is defined in main.py
from models.teacher import Teacher  # Importing the Teacher model for direct database access

@pytest.mark.asyncio
async def test_create_teacher_succeeds():
    """Test creating a new Teacher with valid details."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
        assert response.status_code == 201
        assert "id" in response.json()  # Check if ID is returned
        assert response.json()["message"] == "Teacher created successfully"

@pytest.mark.asyncio
async def test_create_teacher_email_uniqueness_fails():
    """Test creating a Teacher with an email that already exists."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Creating a Teacher for the first time
        await client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
        
        # Attempting to create another Teacher with the same email
        response = await client.post("/teachers", json={"name": "Jane Doe", "email": "john.doe@example.com"})
        assert response.status_code == 400  # Expecting a bad request
        assert response.json() == {
            "error": {
                "code": "E001",
                "message": "Email address is already in use.",
                "details": {}
            }
        }

@pytest.mark.asyncio
async def test_retrieve_teacher_details_succeeds():
    """Test retrieving Teacher details by ID."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a Teacher to retrieve
        create_response = await client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
        teacher_id = create_response.json()["id"]
        
        # Retrieve the Teacher's details
        retrieve_response = await client.get(f"/teachers/{teacher_id}")
        assert retrieve_response.status_code == 200
        assert retrieve_response.json() == {
            "name": "John Doe",
            "email": "john.doe@example.com"
        }

@pytest.mark.asyncio
async def test_create_teacher_missing_fields_fails():
    """Test trying to create a Teacher without required fields."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Attempting to create a Teacher without a name
        response = await client.post("/teachers", json={"email": "john.doe@example.com"})
        assert response.status_code == 400  # Expecting a bad request
        assert response.json() == {
            "error": {
                "code": "E002",
                "message": "Name is required.",
                "details": {}
            }
        }
        
        response = await client.post("/teachers", json={"name": "John Doe"})
        assert response.status_code == 400  # Expecting a bad request
        assert response.json() == {
            "error": {
                "code": "E002",
                "message": "Email is required.",
                "details": {}
            }
        }
```