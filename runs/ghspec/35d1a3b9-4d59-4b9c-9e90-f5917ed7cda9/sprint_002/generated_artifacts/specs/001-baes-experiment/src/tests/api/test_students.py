```python
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from src.api import app  # Import the FastAPI application
from src.repository import init_db, get_session, Student

@pytest.fixture
def client():
    # This fixture provides a test client for making API requests
    with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Setup the database before running the tests
    init_db()  # Initialize the database with necessary schema and data

@pytest.mark.asyncio
async def test_create_student(client):
    # Test creating a student with a valid name and email
    response = await client.post("/api/v1/students", json={"name": "John Doe", "email": "johndoe@example.com"})
    
    assert response.status_code == 201  # Check if student creation returns 201 Created
    assert response.json() == {"message": "Student created successfully."}

@pytest.mark.asyncio
async def test_retrieve_students(client):
    # Test retrieving a list of students including email addresses
    response = await client.get("/api/v1/students")
    
    assert response.status_code == 200  # Check if retrieval returns 200 OK
    students = response.json()
    
    # Check the response structure and data
    assert isinstance(students, list)  # Ensure the response is a list
    assert len(students) > 0  # Ensure there is at least one student
    for student in students:
        assert "id" in student
        assert "name" in student
        assert "email" in student  # Ensure each student has an email address
```