```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Helper function to create a course for testing purposes
def create_course(title: str, description: str):
    response = client.post("/courses/", json={"title": title, "description": description})
    return response.json(), response.status_code

# Helper function to create a teacher for testing purposes
def create_teacher(name: str, email: str):
    response = client.post("/teachers/", json={"name": name, "email": email})
    return response.json(), response.status_code

# Test case for retrieving Course details with Teacher information
def test_get_course_details_with_teacher():
    # First, create a teacher
    teacher_data, _ = create_teacher("Jane Smith", "jane.smith@example.com")
    
    # Then, create a course and assign the teacher
    course_data, _ = create_course("Mathematics", "Description of Mathematics course")
    course_id = course_data["id"]

    # Assign the teacher to the course (assuming the endpoint for assignment is already implemented)
    client.post(f"/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_data["id"]})

    # Now, retrieve the course details
    response = client.get(f"/api/v1/courses/{course_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == course_id
    assert "teacher" in data
    assert data["teacher"]["name"] == teacher_data["name"]

# Test case for retrieving a non-existent Course
def test_get_non_existent_course():
    response = client.get("/api/v1/courses/99999")  # Assuming 99999 doesn't exist
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}
```