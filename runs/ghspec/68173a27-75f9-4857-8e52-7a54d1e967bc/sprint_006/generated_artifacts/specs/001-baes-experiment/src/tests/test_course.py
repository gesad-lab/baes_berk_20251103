```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.repositories.course_repository import CourseRepository
from src.repositories.teacher_repository import TeacherRepository

client = TestClient(app)

def test_assign_teacher_to_course_success():
    # Arrange: Create a course and a teacher to assign
    teacher_response = client.post("/api/v1/teachers", json={"name": "Alice", "email": "alice@example.com"})
    teacher_id = teacher_response.json()["id"]
    
    course_response = client.post("/api/v1/courses", json={"title": "Math 101"})
    course_id = course_response.json()["id"]
    
    # Act: Assign the teacher to the course
    assign_response = client.post(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})
    
    # Assert: Check successful assignment
    assert assign_response.status_code == 200
    assert assign_response.json() == {"message": "Teacher assigned to course successfully."}

def test_assign_teacher_to_course_invalid_teacher_id():
    # Arrange: Create a course
    course_response = client.post("/api/v1/courses", json={"title": "Math 101"})
    course_id = course_response.json()["id"]
    
    # Act: Assign a non-existing teacher to the course
    assign_response = client.post(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": 999})
    
    # Assert: Validate error for invalid teacher ID
    assert assign_response.status_code == 400
    assert assign_response.json() == {"error": {"code": "E002", "message": "Invalid teacher ID.", "details": {}}}

def test_assign_teacher_to_course_invalid_course_id():
    # Arrange: Create a teacher
    teacher_response = client.post("/api/v1/teachers", json={"name": "Bob", "email": "bob@example.com"})
    teacher_id = teacher_response.json()["id"]

    # Act: Assign the teacher to a non-existing course
    assign_response = client.post(f"/api/v1/courses/999/assign_teacher", json={"teacher_id": teacher_id})

    # Assert: Validate error for invalid course ID
    assert assign_response.status_code == 400
    assert assign_response.json() == {"error": {"code": "E003", "message": "Invalid course ID.", "details": {}}}

def test_retrieve_course_with_teacher():
    # Arrange: Create a teacher and a course
    teacher_response = client.post("/api/v1/teachers", json={"name": "Cathy", "email": "cathy@example.com"})
    teacher_id = teacher_response.json()["id"]
    
    course_response = client.post("/api/v1/courses", json={"title": "Science 101"})
    course_id = course_response.json()["id"]

    # Assign the teacher to the course
    client.post(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})

    # Act: Retrieve course details
    course_detail_response = client.get(f"/api/v1/courses/{course_id}")
    
    # Assert: Check if teacher information is included
    assert course_detail_response.status_code == 200
    data = course_detail_response.json()
    assert data["id"] == course_id
    assert data["teacher"]["id"] == teacher_id
    assert data["teacher"]["name"] == "Cathy"
```