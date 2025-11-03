```python
import pytest
from fastapi.testclient import TestClient
from src.services.enrollment_service import EnrollmentService  # Import the EnrollmentService
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup the in-memory database for testing."""
    # Setup logic to create required tables and seed initial data for students and courses
    yield
    # Cleanup logic if necessary

def test_enroll_student_success(setup_database):
    """Test enrolling a student in a course with valid data."""
    response = client.post("/students/1/enroll", json={"courseId": 1})
    assert response.status_code == 201
    assert response.json() == {"studentId": 1, "courseId": 1}

def test_get_courses_for_student_success(setup_database):
    """Test retrieving courses for an enrolled student."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert "courses" in response.json()

def test_enroll_student_nonexistent_student(setup_database):
    """Test enrolling a student that does not exist."""
    response = client.post("/students/999/enroll", json={"courseId": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found"}}

def test_enroll_student_nonexistent_course(setup_database):
    """Test enrolling a student in a course that does not exist."""
    response = client.post("/students/1/enroll", json={"courseId": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}

def test_get_courses_for_nonexistent_student(setup_database):
    """Test retrieving courses for a student that does not exist."""
    response = client.get("/students/999/courses")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found"}}
```