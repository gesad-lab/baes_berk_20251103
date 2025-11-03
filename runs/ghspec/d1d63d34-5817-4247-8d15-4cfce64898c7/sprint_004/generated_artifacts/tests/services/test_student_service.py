```python
import pytest
from fastapi.testclient import TestClient
from src.services.student_service import app, remove_course_from_student
from pydantic import ValidationError

client = TestClient(app)

@pytest.fixture
def sample_student():
    """Fixture for creating a sample student."""
    return {
        "name": "John Doe",
        "courses": ["course_id_1", "course_id_2"]
    }

@pytest.fixture
def create_student(sample_student):
    """Fixture to create a student for testing purposes."""
    response = client.post("/students/", json=sample_student)
    assert response.status_code == 201
    return response.json()["id"]

def test_remove_course_from_student(create_student):
    """Test successful course removal from student."""
    # First, make sure the course was assigned to the student
    response = client.get(f"/students/{create_student}/courses")
    assert response.status_code == 200
    assert len(response.json()) == 2  # Should have 2 courses initially

    # Now, perform the course removal
    course_id = "course_id_1"
    response = client.delete(f"/students/{create_student}/courses/{course_id}")
    assert response.status_code == 204  # No Content

    # Verify the course has been removed successfully
    response = client.get(f"/students/{create_student}/courses")
    assert response.status_code == 200
    assert len(response.json()) == 1  # Should have 1 course left
    assert course_id not in [course["id"] for course in response.json()]  # Ensure the course is indeed removed

def test_remove_course_from_student_course_does_not_exist(create_student):
    """Test removing a course that does not exist for the student."""
    # Trying to remove a non-existent course
    response = client.delete(f"/students/{create_student}/courses/non_existent_course_id")
    assert response.status_code == 404  # Course not found error

def test_remove_course_from_student_invalid_student_id():
    """Test removing a course from an invalid student ID."""
    course_id = "course_id_1"
    response = client.delete(f"/students/999/courses/{course_id}")  # Assuming 999 is an invalid ID
    assert response.status_code == 404  # Student not found error
```