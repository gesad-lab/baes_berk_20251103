```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Course, Teacher

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Set up necessary database state before tests."""
    # You may want to create Course and Teacher records in the setup phase.
    yield
    # Clean up database state after tests

def test_assign_teacher_to_course(setup_database):
    """Test that assigning a teacher to a course updates the course correctly."""
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_get_course_with_teacher(setup_database):
    """Test retrieving course details along with assigned teacher."""
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_update_assigned_teacher(setup_database):
    """Test updating the assigned teacher for a course."""
    response = client.put("/courses/1/update_teacher", json={"teacher_id": 2})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 2

def test_remove_teacher_from_course(setup_database):
    """Test removing a teacher from a course."""
    response = client.delete("/courses/1/remove_teacher")
    assert response.status_code == 200
    assert response.json()["teacher_id"] is None

def test_assign_teacher_to_nonexistent_course(setup_database):
    """Test error handling when assigning a teacher to a non-existent course."""
    response = client.post("/courses/999/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found", "details": {}}}

def test_assign_nonexistent_teacher(setup_database):
    """Test error handling for invalid teacher assignment."""
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Teacher not found", "details": {}}}
```