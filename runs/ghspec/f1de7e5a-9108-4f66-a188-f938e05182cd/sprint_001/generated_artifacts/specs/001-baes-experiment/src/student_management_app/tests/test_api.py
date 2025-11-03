```python
import pytest
from fastapi.testclient import TestClient
from student_management_app.main import app  # Assuming the FastAPI instance is here

client = TestClient(app)

@pytest.fixture(scope="module")
def create_student():
    """Fixture to create a student for testing purposes."""
    response = client.post("/students", json={"name": "John Doe"})
    return response.json()

def test_create_student_success():
    """Test creating a new student with a valid name."""
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 201
    assert "id" in response.json()  # Check if the response contains the student ID
    assert response.json()["name"] == "Jane Doe"  # Check if the name matches

def test_create_student_with_empty_name():
    """Test creating a student with an empty name."""
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name must be a non-empty string."}}  # Adjust according to the actual error response format

def test_create_student_with_missing_name():
    """Test creating a student with missing name field."""
    response = client.post("/students", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Name is required."}}  # Adjust according to the actual error response format

def test_retrieve_students_empty_list(create_student):
    """Test retrieving students when no students have been created."""
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == []  # Expect an empty list since this is a fresh database state

# More integration tests can be added here based on functionality

```