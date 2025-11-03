import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Set up necessary database state before tests."""
    # Assuming we have test data setup functions to create initial states
    # This might involve adding teachers and courses
    yield
    # Clean up database state after tests, if necessary

def test_create_teacher(setup_database):
    """Test creating a teacher."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@school.com"})
    assert response.status_code == 201
    assert "id" in response.json()

def test_assign_teacher_to_course(setup_database):
    """Test assigning a teacher to a course."""
    response = client.put("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1  # Assuming the response includes the updated teacher ID

def test_update_teacher_assignment_for_course(setup_database):
    """Test updating a teacher assignment for a course."""
    response = client.put("/courses/1/assign_teacher", json={"teacher_id": 2})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 2  # Check that the teacher was updated correctly

def test_remove_teacher_from_course(setup_database):
    """Test removing a teacher from a course."""
    response = client.put("/courses/1/remove_teacher")
    assert response.status_code == 200
    assert "teacher_id" not in response.json()  # Ensure the teacher is no longer assigned

def test_assign_teacher_invalid_course(setup_database):
    """Test assigning a teacher to a non-existent course."""
    response = client.put("/courses/999/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}  # Example error response

def test_assign_nonexistent_teacher_to_course(setup_database):
    """Test assigning a non-existent teacher to a course."""
    response = client.put("/courses/1/assign_teacher", json={"teacher_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Teacher not found"}}  # Example error response