```python
import pytest
from httpx import AsyncClient
from src.main import app  # Assuming the FastAPI app is instantiated in main.py
from src.database import init_db, get_db  # Function to initialize and access the database
from src.models import Student  # The Student model should be defined appropriately to match the database schema


@pytest.fixture(scope="module")
async def test_client():
    # Initialize the database before the tests and create the necessary tables
    await init_db()
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_create_student_with_email(test_client):
    # Test case: Adding a new student with valid email
    response = await test_client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    
    # Check if the response status code is 201 Created
    assert response.status_code == 201
    assert response.json() == {"message": "Student created successfully", "id": response.json()["id"]}


@pytest.mark.asyncio
async def test_retrieve_students(test_client):
    # Test case: Retrieving all students
    response = await test_client.get("/students")
    
    # Check if the response status code is 200 OK
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expect a list of students
    assert all("name" in student and "email" in student for student in response.json())  # Check student fields


@pytest.mark.asyncio
async def test_create_student_with_invalid_email(test_client):
    # Test case: Adding a new student with invalid email
    response = await test_client.post("/students", json={"name": "Jane Doe", "email": "invalid-email"})
    
    # Check if the response status code is 400 Bad Request
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format"}}  # Check error message


@pytest.mark.asyncio
async def test_create_student_without_email(test_client):
    # Test case: Adding a new student without an email
    response = await test_client.post("/students", json={"name": "Jack Smith"})
    
    # Check if the response status code is 400 Bad Request
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email is required"}}  # Check error message
```