```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student_course import Student, Course, StudentCourses
from src.services.student_course_service import enroll_student, get_student_courses
from src.repositories.student_course_repository import get_student_enrollment

client = TestClient(app)

# Sample test data for students and courses
valid_student_data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

valid_course_data = {
    "title": "Introduction to Python",
    "description": "A comprehensive course on Python programming."
}

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Setup code to initialize database goes here
    # This can create test instances of Student and Course in the database
    # Cleanup code can also be included after tests
    yield
    # Cleanup code to drop test instances from the database goes here

def test_enroll_student_success():
    """ Test that a student can be successfully enrolled in a course """
    # Create a valid student and course in the database beforehand
    response = client.post("/enroll", json={"student_id": 1, "course_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Student enrolled successfully"}

def test_enroll_student_invalid_course():
    """ Test enrolling a student in a non-existent course """
    response = client.post("/enroll", json={"student_id": 1, "course_id": 9999})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid course ID"}} 

def test_get_student_courses_success():
    """ Test retrieving courses for a student """
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert type(response.json()) == list  # Expecting a list of courses

def test_get_student_courses_no_enrollment():
    """ Test retrieving courses for a student with no enrollments """
    response = client.get("/students/2/courses")
    assert response.status_code == 200
    assert response.json() == []  # Expecting an empty list as response
    
def test_enrollment_redundancy():
    """ Test enrolling the same student in the same course twice """
    client.post("/enroll", json={"student_id": 1, "course_id": 1})  # First enrollment
    response = client.post("/enroll", json={"student_id": 1, "course_id": 1})  # Second enrollment
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Student is already enrolled in this course"}} 
```