```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py
from models import StudentCourses  # Importing the StudentCourses model

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    """Setup test database and clean up after tests."""
    # Code for creating the test database schema can be added here.
    yield
    # Code for tearing down the database can be added here.

def test_assign_course_to_student_success(setup_db):
    """Test assigning a course to a student."""
    response = client.post("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Course assigned successfully."}

def test_assign_course_to_student_invalid_course(setup_db):
    """Test assigning a non-existent course to a student."""
    response = client.post("/students/1/courses", json={"course_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Course not found."}}

def test_get_courses_for_student_success(setup_db):
    """Test retrieving all courses for a specific student."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    # Assuming student 1 is enrolled in course 1 and 2
    assert response.json() == [
        {"id": 1, "name": "Mathematics", "level": "beginner"},
        {"id": 2, "name": "Science", "level": "intermediate"}
    ]

def test_get_courses_for_student_no_courses(setup_db):
    """Test retrieving courses for a student with no enrollments."""
    response = client.get("/students/2/courses")  # Assuming student 2 has no courses
    assert response.status_code == 200
    assert response.json() == []
```