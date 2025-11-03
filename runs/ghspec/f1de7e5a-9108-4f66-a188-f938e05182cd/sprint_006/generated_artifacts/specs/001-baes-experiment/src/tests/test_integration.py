# tests/test_integration.py

import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your main app is in a file called main.py
from models import Course, Student, StudentCourses, Teacher  # Import required models

client = TestClient(app)

# Test case for creating a new teacher
def test_create_teacher():
    teacher_data = {"name": "Mr. Smith", "email": "smith@example.com"}
    response = client.post("/teachers", json=teacher_data)
    assert response.status_code == 201
    assert response.json() == {"id": response.json()["id"], **teacher_data}  # Check that the response includes the created teacher data

# Test case for assigning a teacher to a course
def test_assign_teacher_to_course():
    # Create a test course
    course_data = {"name": "Physics", "level": "10"}
    course_response = client.post("/courses", json=course_data)
    course_id = course_response.json()["id"]

    # Create a test teacher
    teacher_data = {"name": "Ms. Johnson", "email": "johnson@example.com"}
    teacher_response = client.post("/teachers", json=teacher_data)
    teacher_id = teacher_response.json()["id"]

    # Assign teacher to the course
    assignment_response = client.post(f"/courses/{course_id}/assign-teacher", json={"teacher_id": teacher_id})
    assert assignment_response.status_code == 200
    assert assignment_response.json() == {"message": "Teacher assigned successfully"}

    # Verify that the teacher has been assigned correctly by retrieving the course details
    course_details_response = client.get(f"/courses/{course_id}")
    assert course_details_response.status_code == 200
    assert course_details_response.json()["teachers"] == [{"id": teacher_id, **teacher_data}]  # Check for assigned teacher in course details

# Test case for handling a non-existent teacher assignment
def test_assign_non_existent_teacher_to_course():
    # Create a test course
    course_data = {"name": "Biology", "level": "11"}
    course_response = client.post("/courses", json=course_data)
    course_id = course_response.json()["id"]

    # Attempt to assign a non-existent teacher ID
    invalid_teacher_id = 9999
    assignment_response = client.post(f"/courses/{course_id}/assign-teacher", json={"teacher_id": invalid_teacher_id})
    assert assignment_response.status_code == 404  # Expect not found for invalid teacher
    assert assignment_response.json() == {"error": {"code": "E404", "message": "Teacher not found", "details": {}}}

# Additional tests for retrieving course details should go here, following the same pattern.