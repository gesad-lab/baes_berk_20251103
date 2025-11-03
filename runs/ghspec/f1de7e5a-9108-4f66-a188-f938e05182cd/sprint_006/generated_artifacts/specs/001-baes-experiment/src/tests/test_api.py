```python
# tests/test_api.py

import pytest
from fastapi.testclient import TestClient
from main import app  # Adjust based on your main app file name
from models import Student, Course, StudentCourses, Teacher  # Import the necessary models

client = TestClient(app)

# Test case for enrolling a student in a course
def test_enroll_student():
    # Create a test student and course
    student_data = {"name": "Alice", "email": "alice@example.com"}
    course_data = {"name": "Mathematics", "level": "1"}
    response = client.post("/students", json=student_data)
    assert response.status_code == 201
    response = client.post("/courses", json=course_data)
    assert response.status_code == 201

    # Enroll student in the created course
    response = client.post("/courses/{courseId}/enroll", params={"courseId": 1}, json={"student_id": 1})
    assert response.status_code == 200

# Test case for assigning a teacher to a course
def test_assign_teacher_to_course():
    # Create a test teacher and course
    teacher_data = {"name": "Ms. Johnson", "email": "johnson@example.com"}
    course_data = {"name": "Science", "level": "2"}
    client.post("/teachers", json=teacher_data)   # Assuming this endpoint exists
    response = client.post("/courses", json=course_data)
    assert response.status_code == 201

    # Assign the created teacher to the created course
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully"}

# Test case for viewing course with teacher information
def test_view_course_with_teacher():
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()  # Assuming response includes this key
    assert response.json()["teacher"]["name"] == "Ms. Johnson"

# Test case for validation of teacher assignment with non-existent teacher
def test_assign_non_existent_teacher():
    course_data = {"name": "English", "level": "2"}
    client.post("/courses", json=course_data)  # Create a course
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 999})  # Invalid teacher ID
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Teacher not found", "details": {}}}
```