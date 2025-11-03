import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    """Fixture for the test client."""
    with TestClient(app) as client:
        yield client

def test_assign_teacher_to_course(client):
    """Test assigning a teacher to an existing course."""
    response = client.patch("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Teacher assigned successfully.",
        "course_id": 1,
        "teacher_id": 1
    }

def test_assign_teacher_to_nonexistent_course(client):
    """Test attempting to assign a teacher to a non-existent course."""
    response = client.patch("/courses/9999/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json() == {
        "error": {"code": "E001", "message": "Course not found."}
    }

def test_get_course_details(client):
    """Test retrieving course details including assigned teacher."""
    response = client.get("/courses/1")
    assert response.status_code == 200
    # Assuming teacher details are available within the response
    assert "teacher" in response.json()

def test_remove_teacher_from_course(client):
    """Test removing a teacher from an existing course."""
    response = client.patch("/courses/1/remove-teacher")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Teacher removed successfully from the course."
    }

def test_remove_teacher_from_nonexistent_course(client):
    """Test removing a teacher from a non-existent course."""
    response = client.patch("/courses/9999/remove-teacher")
    assert response.status_code == 404
    assert response.json() == {
        "error": {"code": "E001", "message": "Course not found."}
    }