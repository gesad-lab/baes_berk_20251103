```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py

@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

def test_assign_teacher_to_course(client):
    """Test assigning a teacher to a course successfully."""
    # Create a teacher
    teacher_response = client.post("/teachers", json={"name": "Alice Smith", "email": "alice.smith@example.com"})
    assert teacher_response.status_code == 201
    teacher_id = teacher_response.json()["id"]

    # Create a course
    course_response = client.post("/courses", json={"title": "Mathematics 101", "description": "Basic math course"})
    assert course_response.status_code == 201
    course_id = course_response.json()["id"]

    # Assign teacher to course
    assign_response = client.post(f"/courses/{course_id}/assignTeacher", json={"teacher_id": teacher_id})
    assert assign_response.status_code == 200
    assert assign_response.json()["teacher_id"] == teacher_id

def test_get_course_with_teacher(client):
    """Test retrieving a course with assigned teacher details."""
    # Create a teacher
    teacher_response = client.post("/teachers", json={"name": "Bob Johnson", "email": "bob.johnson@example.com"})
    assert teacher_response.status_code == 201
    teacher_id = teacher_response.json()["id"]

    # Create a course
    course_response = client.post("/courses", json={"title": "Biology 101", "description": "Introductory biology course"})
    assert course_response.status_code == 201
    course_id = course_response.json()["id"]

    # Assign teacher to course
    assign_response = client.post(f"/courses/{course_id}/assignTeacher", json={"teacher_id": teacher_id})
    assert assign_response.status_code == 200

    # Get course details
    get_course_response = client.get(f"/courses/{course_id}")
    assert get_course_response.status_code == 200
    course_data = get_course_response.json()
    assert course_data["teacher_id"] == teacher_id  # Check if teacher is correctly assigned

def test_update_teacher_assignment(client):
    """Test updating the teacher assignment for a course."""
    # Create two teachers
    teacher_1_response = client.post("/teachers", json={"name": "Emma Brown", "email": "emma.brown@example.com"})
    assert teacher_1_response.status_code == 201
    teacher_1_id = teacher_1_response.json()["id"]

    teacher_2_response = client.post("/teachers", json={"name": "Liam Davis", "email": "liam.davis@example.com"})
    assert teacher_2_response.status_code == 201
    teacher_2_id = teacher_2_response.json()["id"]

    # Create a course
    course_response = client.post("/courses", json={"title": "Chemistry 101", "description": "Fundamentals of chemistry"})
    assert course_response.status_code == 201
    course_id = course_response.json()["id"]

    # Assign the first teacher
    assign_response = client.post(f"/courses/{course_id}/assignTeacher", json={"teacher_id": teacher_1_id})
    assert assign_response.status_code == 200

    # Update to assign the second teacher
    update_response = client.put(f"/courses/{course_id}/assignTeacher", json={"teacher_id": teacher_2_id})
    assert update_response.status_code == 200
    assert update_response.json()["teacher_id"] == teacher_2_id  # Verify the teacher has been updated
```