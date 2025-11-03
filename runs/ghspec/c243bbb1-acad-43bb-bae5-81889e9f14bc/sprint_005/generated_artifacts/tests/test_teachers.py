```python
# tests/test_teachers_api.py

import httpx
import pytest

BASE_URL = "http://localhost:8000/api/v1/teachers"

@pytest.mark.asyncio
async def test_create_teacher_with_valid_data():
    """Test creating a teacher with valid name and email."""
    teacher_data = {
        "name": "John Doe",
        "email": "john@example.com"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=teacher_data)
        assert response.status_code == 201  # Expect created status
        response_data = response.json()
        assert "id" in response_data  # Check if ID is returned
        assert response_data["message"] == "Teacher created successfully"  # Success message

@pytest.mark.asyncio
async def test_get_teacher_details():
    """Test retrieving a teacher's details."""
    teacher_id = 1  # Assuming this teacher exists and has ID 1

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{teacher_id}")
        assert response.status_code == 200  # Expect OK status
        response_data = response.json()
        assert response_data["name"] == "John Doe"  # Check for correct name
        assert response_data["email"] == "john@example.com"  # Check for correct email

@pytest.mark.asyncio
async def test_create_teacher_with_missing_fields():
    """Test response for creating a teacher without required fields."""
    teacher_data = {
        "name": "",  # Missing email
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=teacher_data)
        assert response.status_code == 400  # Expect bad request status
        response_data = response.json()
        assert response_data["error"]["code"] == "E001"  # Specific error code
        assert "email" in response_data["error"]["message"]  # Check for missing field message
```