```python
import json
import pytest
from fastapi.testclient import TestClient
from src.api.course import app  # Assuming 'app' is the FastAPI instance for course
from src.db.models import Course, Student, StudentCourse  # Import necessary models
from src.validations.course_validators import validate_course_input  # Import the validation function

client = TestClient(app)

@pytest.fixture
def valid_course():
    """Fixture to return valid course data."""
    return {"name": "Introduction to Programming", "level": "Beginner"}

@pytest.fixture
def valid_student():
    """Fixture to return a valid student data."""
    return {"name": "John Doe"}

def test_get_student_courses(client, valid_student):
    """Test retrieving courses associated with a student."""
    # First, create a student to associate courses with
    response = client.post("/students", json=valid_student)
    assert response.status_code == 201
    student_id = response.json()["id"]

    # Now, create a couple of courses and associate them with the student
    course1 = {"name": "Introduction to AI", "level": "Intermediate"}
    course2 = {"name": "Data Structures", "level": "Advanced"}
    
    # Create courses
    client.post("/courses", json=course1)
    client.post("/courses", json=course2)
    
    # Assuming we have a PATCH endpoint to associate courses with a student
    response = client.patch(f"/students/{student_id}", json={"course_ids": [1, 2]})
    assert response.status_code == 200

    # Now fetch the student's courses
    response = client.get(f"/students/{student_id}/courses")
    
    # Validate the response is as expected
    assert response.status_code == 200
    courses = response.json()
    
    # Check if the associated courses are returned correctly
    assert len(courses) == 2  # We added two courses
    assert all('id' in course and 'name' in course and 'level' in course for course in courses)

def test_get_student_courses_invalid_student(client):
    """Test retrieving courses for a non-existent student."""
    response = client.get("/students/999/courses")  # Assuming 999 does not exist
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}
```