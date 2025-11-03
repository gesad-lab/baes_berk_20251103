```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel
from src.api.enrollment import app  # Import the relevant FastAPI app instance
from src.models.student import Student
from src.models.course import Course
from src.models.enrollment import Enrollment

client = TestClient(app)

# Sample data for testing
@pytest.fixture(scope="module")
def test_data():
    # Setup: Create a student and a course in the database (mocked)
    student = {"id": 1, "name": "John Doe"}
    course = {"id": 1, "name": "Mathematics", "level": "Beginner"}
    enrollments = []
    
    # Mimic inserting to a database
    yield {
        "student": student,
        "course": course,
        "enrollments": enrollments
    }

def test_enroll_student(test_data):
    # Prepare the request to enroll a student in a course
    response = client.post("/enrollments", json={"student_id": test_data["student"]["id"], "course_id": test_data["course"]["id"]})
    
    # Validate the response
    assert response.status_code == 201
    assert "courses" in response.json()  # The response should include courses
    assert len(response.json()["courses"]) == 1  # One course should be enrolled

def test_enroll_student_invalid_course(test_data):
    # Make a request to enroll a student with an invalid course ID
    response = client.post("/enrollments", json={"student_id": test_data["student"]["id"], "course_id": 999})
    
    # Validate the error response
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Course ID not found."}}

def test_get_student_courses(test_data):
    # First enroll the student to ensure they have courses
    client.post("/enrollments", json={"student_id": test_data["student"]["id"], "course_id": test_data["course"]["id"]})
    
    # Now retrieve the courses for the student
    response = client.get(f"/students/{test_data['student']['id']}/courses")
    
    # Validate the response
    assert response.status_code == 200
    assert len(response.json()) == 1  # The student should have one course

def test_get_student_courses_not_found(test_data):
    # Attempt to retrieve courses for a non-existing student
    response = client.get("/students/999/courses")
    
    # Validate the error response
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student not found."}}
```