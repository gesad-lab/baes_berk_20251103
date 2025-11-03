```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is instantiated in src/main.py
from src.models import Student  # Assuming the Student model is located in src/models.py

client = TestClient(app)

@pytest.fixture(scope="module")
def create_student():
    # Setup: Create a student in the database
    response = client.post("/students/", json={"name": "Test Student", "email": "test@example.com"})
    yield response.json()
    # Teardown: Remove the created student record
    client.delete(f"/students/{response.json()['id']}")

def test_create_student_with_email():
    """Test creating a student with a valid email address."""
    response = client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": response.json()['id'], "name": "John Doe", "email": "john.doe@example.com"}

def test_retrieve_students_includes_email():
    """Test retrieving all students includes their email addresses."""
    response = client.get("/students/")
    assert response.status_code == 200
    for student in response.json():
        assert "email" in student

def test_update_student_email():
    """Test updating a student's email."""
    # First, create a student
    student_response = client.post("/students/", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    student_id = student_response.json()['id']
    
    # Update the student's email
    update_response = client.put(f"/students/{student_id}", json={"email": "jane.new@example.com"})
    assert update_response.status_code == 200
    assert update_response.json() == {"id": student_id, "name": "Jane Doe", "email": "jane.new@example.com"}

def test_create_student_with_invalid_email():
    """Test creating a student with an invalid email returns an error."""
    response = client.post("/students/", json={"name": "Invalid Email", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format."}}
```