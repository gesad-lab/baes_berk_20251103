```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Main FastAPI application
from src.database import get_database  # Assuming there is a function to get the database
from src.models import EnrollmentCreate  # Import the EnrollmentCreate model

client = TestClient(app)

# Integration tests for the enrollment services
@pytest.mark.integration
def test_enroll_student_in_course_valid():
    """Test enrolling a student in a course with valid data."""
    # Given a student ID and a course ID
    student_id = 1  # Assume this student exists
    course_id = 101  # Assume this course exists

    # When sending the enrollment request
    response = client.post("/students/{}/courses".format(student_id), json={"course_id": course_id})

    # Then the response should be successful, confirming the enrollment
    assert response.status_code == 200
    assert response.json() == {"message": "Enrollment successful"}

@pytest.mark.integration
def test_enroll_student_in_course_missing_course_id():
    """Test enrolling a student when course_id is missing."""
    # Given a student ID but without a course ID
    student_id = 1  # Assume this student exists

    # When sending the enrollment request without course_id
    response = client.post("/students/{}/courses".format(student_id), json={})

    # Then the response should return a 400 error
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "course_id is required"}}

@pytest.mark.integration
def test_list_courses_for_student_valid():
    """Test retrieving a list of courses for a specific student."""
    # Given a student ID
    student_id = 1  # Assume this student is enrolled in some courses

    # When sending the request to retrieve courses
    response = client.get("/students/{}/courses".format(student_id))

    # Then the response should return a list of courses for the student
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # The response should be a list
    assert all("course_name" in course for course in response.json())  # Each course should have a name

@pytest.mark.integration
def test_list_courses_for_student_no_courses():
    """Test retrieving courses for a student with no enrollments."""
    student_id = 2  # Assume this student has no enrolled courses

    response = client.get("/students/{}/courses".format(student_id))
    
    assert response.status_code == 200
    assert response.json() == []  # Should return an empty list for no courses

```