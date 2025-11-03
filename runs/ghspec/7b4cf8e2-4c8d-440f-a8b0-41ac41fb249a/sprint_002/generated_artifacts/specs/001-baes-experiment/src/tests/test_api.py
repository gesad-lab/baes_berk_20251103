```python
import pytest
from fastapi.testclient import TestClient
from src.api import app
from src.service import get_student, create_student, update_student

client = TestClient(app)

# Sample test data
student_id_to_delete = 1  # Assuming this ID is valid and exists beforehand

@pytest.fixture
def setup_student():
    """Fixture to create a sample student for tests."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    student_data = response.json()
    yield student_data  # This will provide the created student data for the tests

def test_create_student_with_valid_email():
    """Test case for creating a student with a valid email."""
    response = client.post("/students", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201  # Check if creation was successful
    assert response.json()["email"] == "jane.doe@example.com"

def test_create_student_with_invalid_email():
    """Test case for creating a student with an invalid email."""
    response = client.post("/students", json={"name": "Invalid Email", "email": "invalid-email"})
    assert response.status_code == 400  # Check for bad request
    assert response.json()["error"]["message"] == "Invalid email format"

def test_retrieve_student_with_email(setup_student):
    """Test case for retrieving student details, includes email address."""
    response = client.get(f"/students/{setup_student['id']}")
    assert response.status_code == 200  # Check if retrieval was successful
    assert response.json()["email"] == setup_student["email"]

def test_update_student_email(setup_student):
    """Test case for updating a student's email address."""
    new_email = "new.email@example.com"
    response = client.put(f"/students/{setup_student['id']}", json={"email": new_email})
    assert response.status_code == 200  # Check if the update was successful
    assert response.json()["email"] == new_email

def test_update_student_with_invalid_email(setup_student):
    """Test case for updating student with an invalid email."""
    response = client.put(f"/students/{setup_student['id']}", json={"email": "invalid-email"})
    assert response.status_code == 400  # Check for bad request
    assert response.json()["error"]["message"] == "Invalid email format"
```