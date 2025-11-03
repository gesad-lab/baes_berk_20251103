```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Set up any necessary database state before tests
    yield
    # Clean up database state after tests

def test_enroll_student_success(setup_database):
    """Test that enrolling a student in a course successfully returns the updated student object."""
    response = client.post("/students/1/enroll", json={"course_id": 1})
    assert response.status_code == 200
    assert "success" in response.json()

def test_retrieve_student_courses(setup_database):
    """Test retrieving a student's courses successfully."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_remove_student_from_course_success(setup_database):
    """Test that removing a student from a course successfully returns a success message."""
    response = client.post("/students/1/remove", json={"course_id": 1})
    assert response.status_code == 200
    assert "success" in response.json()

def test_remove_student_from_non_existing_course(setup_database):
    """Test that removing a student from a non-existing course returns a 404 error."""
    response = client.post("/students/1/remove", json={"course_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found", "details": {}}}
```