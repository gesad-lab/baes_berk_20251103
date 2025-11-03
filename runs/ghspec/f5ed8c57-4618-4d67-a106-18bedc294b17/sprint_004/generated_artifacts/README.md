```python
import pytest
from fastapi.testclient import TestClient
from src.api.student_course_api import app  # FastAPI instance for student_course_api
from src.database import get_db, Database  # Assuming there's a database module
from src.models import StudentCourse  # Importing the StudentCourse model

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    # Create a new in-memory database or use a test database
    test_db = Database()
    test_db.create_tables()
    yield test_db
    test_db.drop_tables()

def test_assign_student_to_course(db):
    """Test assigning a student to a course."""
    response = client.post("/assign_student", json={"student_id": 1, "course_id": 1})
    assert response.status_code == 201
    assert response.json() == {"message": "Student assigned to course."}

def test_assign_student_to_course_invalid_student(db):
    """Test assigning student to course with invalid student_id."""
    response = client.post("/assign_student", json={"student_id": 999, "course_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Invalid student ID."}}

def test_assign_student_to_course_invalid_course(db):
    """Test assigning student to course with invalid course_id."""
    response = client.post("/assign_student", json={"student_id": 1, "course_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Invalid course ID."}}

def test_get_students_in_course(db):
    """Test retrieving all students in a course."""
    response = client.get("/course/1/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of students

def test_get_students_in_course_not_found(db):
    """Test retrieving students in a course that doesn't exist."""
    response = client.get("/course/999/students")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Course not found."}}
```