import pytest
from fastapi.testclient import TestClient
from src.api import app
from src.service import get_student, delete_student, create_student

client = TestClient(app)

# Sample test data
student_id_to_delete = 1  # Assuming this ID is valid and exists beforehand

@pytest.fixture
def setup_student():
    # Create a student to ensure we have one for deletion tests
    response = client.post("/students", json={"name": "John Doe"})
    yield response.json()  # This will provide the created student data for tests
    # Teardown code could go here to delete the student if needed

def test_delete_student_success(setup_student):
    """Test deleting a student successfully."""
    student_id = setup_student['id']
    
    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 204  # No Content status for successful delete

    # Verify that the student no longer exists
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 404  # Not Found status means deletion was successful


def test_delete_nonexistent_student():
    """Test attempting to delete a student that does not exist."""
    invalid_student_id = 99999  # Assuming this ID does not exist
    response = client.delete(f"/students/{invalid_student_id}")
    
    assert response.status_code == 404  # Not Found status for nonexistent student
    assert response.json() == {"error": {"code": "E002", "message": "Student not found", "details": {}}}


def test_delete_student_with_invalid_id():
    """Test attempting to delete a student with an invalid ID."""
    invalid_student_id = "abc"  # Using a non-numeric ID
    response = client.delete(f"/students/{invalid_student_id}")
    
    assert response.status_code == 400  # Bad Request status due to invalid ID format
    assert response.json() == {"error": {"code": "E001", "message": "Invalid student ID", "details": {}}}