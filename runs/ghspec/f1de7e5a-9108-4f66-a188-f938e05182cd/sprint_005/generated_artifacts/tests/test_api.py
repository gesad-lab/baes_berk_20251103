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
    course_data = {"name": "Mathematics", "level": "Beginner"}
    
    # Enroll the student in the course
    response = client.post("/students", json=student_data)
    assert response.status_code == 201
    student_id = response.json().get("id")

    response = client.post(f"/courses/{student_id}/enroll", json=course_data)
    assert response.status_code == 200
    
# Test case for creating a new teacher
def test_create_teacher():
    teacher_data = {"name": "John Smith", "email": "john.smith@example.com"}  # Valid teacher data
    
    response = client.post("/teachers", json=teacher_data)
    assert response.status_code == 201  # Check if teacher is successfully created
    assert response.json()["name"] == teacher_data["name"]  # Validate that the returned name is correct
    assert response.json()["email"] == teacher_data["email"]  # Validate that the returned email is correct

# Test case for retrieving teacher details
def test_view_teacher_details():
    response = client.get("/teachers")
    assert response.status_code == 200  # Ensure the request is successful
    teachers = response.json()  # Get the list of teachers
    assert isinstance(teachers, list)  # Validate the response is a list
    assert len(teachers) > 0  # Check that the list is not empty
    
    # Further validation of structure of returned teachers
    for teacher in teachers:
        assert "id" in teacher  # Ensure teacher has an id
        assert "name" in teacher  # Ensure teacher has a name
        assert "email" in teacher  # Ensure teacher has an email

# Test case for creating teacher without required fields
def test_create_teacher_without_required_fields():
    invalid_teacher_data = {"name": ""}  # Missing email
    
    response = client.post("/teachers", json=invalid_teacher_data)
    assert response.status_code == 422  # Check for validation error
    assert response.json()["detail"][0]["msg"] == "field required"  # Check the specific error message
```