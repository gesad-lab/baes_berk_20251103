```python
import json
import pytest
from fastapi.testclient import TestClient
from src.api.student import app  # Assuming 'app' is the FastAPI instance

client = TestClient(app)

@pytest.fixture
def sample_student():
    """Fixture to return a sample student data"""
    return {"name": "John Doe"}

def test_add_student_success(sample_student):
    """Test adding a new student successfully."""
    response = client.post("/students/", json=sample_student)
    assert response.status_code == 201  # Expecting 201 Created
    response_data = response.json()
    assert response_data["name"] == sample_student["name"]

def test_retrieve_students_success(sample_student):
    """Test retrieving all students returns correct data format."""
    # First add a student
    client.post("/students/", json=sample_student)
    
    # Now retrieve all students
    response = client.get("/students/")
    assert response.status_code == 200  # Expecting 200 OK
    response_data = response.json()
    
    # Check that the response is a list
    assert isinstance(response_data, list)
    assert len(response_data) > 0  # Ensure we have items in the list

    # Verify the student information is as expected
    assert response_data[0]["name"] == sample_student["name"]

def test_add_student_without_name():
    """Test that adding a student without a name returns an error."""
    response = client.post("/students/", json={})  # No name provided
    assert response.status_code == 400  # Expecting 400 Bad Request
    response_data = response.json()
    
    # Check for correct error message in the response
    assert response_data["error"]["code"] == "E001"
    assert "name" in response_data["error"]["message"]
    assert "required" in response_data["error"]["message"]

```