```python
# tests/test_api.py

import pytest
from fastapi.testclient import TestClient
from main import app  # Adjust based on your main app file name
from models import Student, Course, StudentCourses  # Import the necessary models

client = TestClient(app)

# Test case for enrolling a student in a course
def test_enroll_student():
    # Create a test student and course
    student_data = {"name": "Alice", "email": "alice@example.com"}
    course_data = {"name": "Mathematics", "level": "Beginner"}
    
    # Create student
    response = client.post("/students", json=student_data)
    assert response.status_code == 201
    student_id = response.json()["id"]  # Get the created student's ID
    
    # Create course
    response = client.post("/courses", json=course_data)
    assert response.status_code == 201
    course_id = response.json()["id"]  # Get the created course's ID
    
    # Enroll the student in the course
    enroll_response = client.post(f"/enroll", json={"student_id": student_id, "course_id": course_id})
    assert enroll_response.status_code == 200
    assert enroll_response.json() == {"message": "Student enrolled successfully"}

    # Verify the association in the database (if needed)

# Test case for invalid course enrollment
def test_enroll_student_invalid_course():
    student_data = {"name": "Bob", "email": "bob@example.com"}
    response = client.post("/students", json=student_data)
    assert response.status_code == 201
    student_id = response.json()["id"]  # Get the created student's ID
    
    # Attempt to enroll the student in a non-existent course
    enroll_response = client.post("/enroll", json={"student_id": student_id, "course_id": 9999})  # Invalid course ID
    assert enroll_response.status_code == 400
    assert enroll_response.json() == {"error": {"code": "E001", "message": "Invalid course ID", "details": {}}}

# Test case for retrieving courses for a student
def test_get_courses_for_student():
    student_data = {"name": "Charlie", "email": "charlie@example.com"}
    response = client.post("/students", json=student_data)
    assert response.status_code == 201
    student_id = response.json()["id"]  # Create Charlie

    # Create a course for Charlie to enroll
    course_data = {"name": "Science", "level": "Intermediate"}
    response = client.post("/courses", json=course_data)
    assert response.status_code == 201
    course_id = response.json()["id"]  # Create Science course

    # Enroll Charlie in Science course
    enroll_response = client.post("/enroll", json={"student_id": student_id, "course_id": course_id})
    assert enroll_response.status_code == 200

    # Retrieve courses for Charlie
    courses_response = client.get(f"/students/{student_id}/courses")
    assert courses_response.status_code == 200
    assert len(courses_response.json()) == 1  # Expecting one course
    assert courses_response.json()[0]["name"] == "Science"
```