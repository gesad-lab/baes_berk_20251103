```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assume the FastAPI app is instantiated in a file named main.py

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    # Setup the database: create tables as necessary before tests
    # This would normally include dropping any existing tables and re-creating them
    pass  # Replace with actual setup code

def test_create_student_missing_name():
    # Test creating a student without providing a name
    response = client.post("/students", json={"email": "test@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required."}}

def test_create_student_with_valid_email():
    # Test creating a student with valid name and email
    response = client.post("/students", json={"name": "Test Student", "email": "test@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Test Student", "email": "test@example.com"}

def test_create_student_missing_email():
    # Test creating a student without providing an email
    response = client.post("/students", json={"name": "Test Student"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email is required."}}

def test_create_student_with_invalid_email_format():
    # Test creating a student with an invalid email format
    response = client.post("/students", json={"name": "Test Student", "email": "invalid_email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E003", "message": "Invalid email format."}}

def test_get_student_by_id():
    # Test retrieving a student by ID
    response = client.post("/students", json={"name": "Test Student", "email": "test@example.com"})
    student_id = response.json()["id"]
    
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json() == {"id": student_id, "name": "Test Student", "email": "test@example.com"}
```