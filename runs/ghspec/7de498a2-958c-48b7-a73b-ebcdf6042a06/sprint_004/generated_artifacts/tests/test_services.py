```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.services import enroll_student_in_course, remove_student_from_course, get_student_courses
from pydantic import BaseModel

@pytest.fixture(scope="module")
def test_client():
    """Create a test client for the FastAPI application."""
    client = TestClient(app)
    yield client

class CourseCreate(BaseModel):
    name: str  # The name of the course
    level: str  # The level of the course, required field

class CourseResponse(BaseModel):
    id: int  # The ID of the course
    name: str  # The name of the course
    level: str  # The level of the course

class StudentCourse(BaseModel):
    student_id: int
    course_id: int

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    """Set up any necessary database state before each test."""
    # Add setup logic if necessary, such as creating test data
    yield
    # Clean up database state after tests if necessary

def test_enroll_student_in_course():
    """Test successful enrollment of a student in a course."""
    response = enroll_student_in_course(student_id=1, course_id=1)
    assert response["status"] == "success"
    assert response["message"] == "Student enrolled in course"

def test_remove_student_from_course():
    """Test successful removal of a student from a course."""
    response = remove_student_from_course(student_id=1, course_id=1)
    assert response["status"] == "success"
    assert response["message"] == "Student removed from course"

def test_get_student_courses():
    """Test fetching courses for a student."""
    response = get_student_courses(student_id=1)
    assert isinstance(response, list)
    assert len(response) >= 0  # Ensure a list is returned

    if response:
        assert all("course_id" in course for course in response)  # Each course should have a course_id
```