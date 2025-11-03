```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Helper function to create a teacher for testing purposes
def create_teacher(name: str, email: str):
    response = client.post("/teachers/", json={"name": name, "email": email})
    return response.json(), response.status_code

# Test case for creating a new Teacher record
def test_create_teacher():
    teacher_data, status_code = create_teacher("John Doe", "john.doe@example.com")
    assert status_code == 201  # Check for successful creation
    assert teacher_data["name"] == "John Doe"
    assert teacher_data["email"] == "john.doe@example.com"

# Test case for retrieving a Teacher's data
def test_retrieve_teacher():
    teacher_data, _ = create_teacher("Jane Smith", "jane.smith@example.com")
    teacher_id = teacher_data["id"]  # Assume the created teacher response includes an id

    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200  # Check for successful retrieval
    assert response.json()["name"] == "Jane Smith"
    assert response.json()["email"] == "jane.smith@example.com"

# Test case for attempting to create a Teacher with missing fields
def test_create_teacher_missing_fields():
    response = client.post("/teachers/", json={"name": ""})  # Missing email
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"error": {"code": "E001", "message": "Email must be provided"}}  # Adjust error message as needed

    response = client.post("/teachers/", json={"email": ""})  # Missing name
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"error": {"code": "E001", "message": "Name must be provided"}}  # Adjust error message as needed

# Test case for ensuring existing Student and Course records remain intact
def test_existing_records_integrity():
    # Create a student for testing
    student_response = client.post("/students/", json={"name": "Student A"})
    student_id = student_response.json()["id"]

    # Create a course for testing
    course_response = client.post("/courses/", json={"name": "Course A", "level": "Beginner"})
    course_id = course_response.json()["id"]

    # Verify that the student and course details are still retrievable
    student_retrieval = client.get(f"/students/{student_id}")
    assert student_retrieval.status_code == 200
    assert student_retrieval.json()["name"] == "Student A"

    course_retrieval = client.get(f"/courses/{course_id}")
    assert course_retrieval.status_code == 200
    assert course_retrieval.json()["name"] == "Course A"
```