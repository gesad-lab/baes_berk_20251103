import httpx
import pytest

BASE_URL = "http://localhost:8000/api/v1/students"

@pytest.mark.asyncio
async def test_create_student_with_valid_data():
    """Test creating a student with valid data."""
    student_data = {
        "name": "John Doe",
        "age": 20,
        "email": "john.doe@example.com"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=student_data)
        
    assert response.status_code == 201
    assert response.json().get("email") == student_data["email"]

@pytest.mark.asyncio
async def test_create_student_with_invalid_email():
    """Test creating a student with an invalid email format."""
    student_data = {
        "name": "Jane Doe",
        "age": 22,
        "email": "jane.doe@invalid"  # Invalid email
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=student_data)

    assert response.status_code == 400
    assert "error" in response.json()
    assert response.json()["error"]["code"] == "E001"  # Specific error code for invalid email

@pytest.mark.asyncio
async def test_get_student_by_id():
    """Test retrieving a student by their ID."""
    
    # Assume a student with ID 1 exists
    student_id = 1
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{student_id}")
        
    assert response.status_code == 200
    student = response.json()
    assert student["id"] == student_id
    assert "name" in student
    assert "email" in student

@pytest.mark.asyncio
async def test_get_non_existing_student():
    """Test retrieving a student that does not exist."""
    
    non_existing_id = 9999  # Assuming this ID does not exist
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{non_existing_id}")

    assert response.status_code == 404
    assert "error" in response.json()
    assert response.json()["error"]["message"] == "Student not found"  # Check appropriate error message

@pytest.mark.asyncio
async def test_update_student_email():
    """Test updating an existing student's email."""
    
    student_id = 1  # Assume this ID exists
    updated_data = {
        "email": "new.email@example.com"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/{student_id}", json=updated_data)
        
    assert response.status_code == 200
    assert response.json().get("email") == updated_data["email"]

@pytest.mark.asyncio
async def test_delete_student():
    """Test deleting a student by ID."""
    
    student_id = 1  # Assume this ID exists
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/{student_id}")
        
    assert response.status_code == 204  # No content returned on successful delete

    # Verify that the student is actually deleted by trying to retrieve them
    response = await client.get(f"{BASE_URL}/{student_id}")
    assert response.status_code == 404
    assert "error" in response.json()