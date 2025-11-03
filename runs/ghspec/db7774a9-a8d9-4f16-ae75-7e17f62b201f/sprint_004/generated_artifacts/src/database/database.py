```python
# tests/test_student_course.py

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_assign_courses_to_student():
    """Test assigning one or more courses to a student."""
    # Create a student first
    student_response = client.post("/students", json={"name": "John Doe"})
    student_id = student_response.json()["id"]

    # Create courses to assign
    course_response_1 = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    course_response_2 = client.post("/courses", json={"name": "Science 101", "level": "Intermediate"})
    
    # Get course IDs
    course_id_1 = course_response_1.json()["id"]
    course_id_2 = course_response_2.json()["id"]

    # Assign courses to the student
    response = client.post(f"/students/{student_id}/assign_courses", json={"course_ids": [course_id_1, course_id_2]})
    
    assert response.status_code == 200
    assert "updated_student" in response.json()
    assert response.json()["updated_student"]["id"] == student_id
    assert len(response.json()["updated_student"]["courses"]) == 2

def test_get_student_with_courses():
    """Test retrieving a student along with their assigned courses."""
    student_response = client.post("/students", json={"name": "Jane Doe"})
    student_id = student_response.json()["id"]

    course_response = client.post("/courses", json={"name": "History 101", "level": "Beginner"})
    course_id = course_response.json()["id"]

    # Assign a course to the student
    client.post(f"/students/{student_id}/assign_courses", json={"course_ids": [course_id]})

    # Retrieve student data
    response = client.get(f"/students/{student_id}")
    
    assert response.status_code == 200
    assert response.json()["id"] == student_id
    assert len(response.json()["courses"]) == 1
    assert response.json()["courses"][0]["id"] == course_id

def test_list_students_with_courses():
    """Test listing all students with their enrolled courses."""
    response = client.get("/students")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of students

def test_assign_courses_missing_student_id():
    """Test error handling when student ID is missing."""
    response = client.post("/students//assign_courses", json={"course_ids": [1, 2]})
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Missing student ID"

def test_assign_courses_invalid_course_ids():
    """Test error handling for invalid course ID assignment."""
    student_response = client.post("/students", json={"name": "Bob Smith"})
    student_id = student_response.json()["id"]

    response = client.post(f"/students/{student_id}/assign_courses", json={"course_ids": ["invalid_id"]})
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid course IDs"
```