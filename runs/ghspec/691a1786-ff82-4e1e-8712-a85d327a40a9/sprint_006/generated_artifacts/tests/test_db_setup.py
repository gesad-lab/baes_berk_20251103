```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src.main import app
from src.models.course import Course
from src.models.teacher import Teacher
from src.db.database import get_db

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def test_db():
    # Setup code for initializing the database
    # Create a new database session and a test table structure...
    pass

def test_create_course_with_teacher(test_client, test_db):
    # Create a mock teacher to associate with the course
    mock_teacher = {
        "name": "John Doe",
        "subject": "Mathematics"
    }
    response = test_client.post("/teachers/", json=mock_teacher)
    assert response.status_code == 201
    teacher_id = response.json()["id"]

    course_data = {
        "name": "Algebra 101",
        "description": "Introductory algebra course",
        "teacher_id": teacher_id
    }
    
    response = test_client.post("/courses/", json=course_data)
    assert response.status_code == 201
    assert response.json()["teacher_id"] == teacher_id
    assert response.json()["name"] == "Algebra 101"

def test_associate_teacher_to_course(test_client, test_db):
    # Create a mock course and teacher first
    mock_teacher = {
        "name": "Jane Smith",
        "subject": "Physics"
    }
    response = test_client.post("/teachers/", json=mock_teacher)
    assert response.status_code == 201
    teacher_id = response.json()["id"]
    
    course_data = {
        "name": "Physics Basics",
        "description": "Basic concepts of physics",
        "teacher_id": teacher_id
    }
    response = test_client.post("/courses/", json=course_data)
    assert response.status_code == 201
    course_id = response.json()["id"]

    # Now associate another teacher to the existing course
    new_teacher_data = {
        "name": "Emily Davis",
        "subject": "Chemistry"
    }
    response = test_client.post("/teachers/", json=new_teacher_data)
    assert response.status_code == 201
    new_teacher_id = response.json()["id"]

    # Update the course with the new teacher
    updated_course_data = {
        "teacher_id": new_teacher_id
    }
    response = test_client.put(f"/courses/{course_id}/", json=updated_course_data)
    assert response.status_code == 200
    assert response.json()["teacher_id"] == new_teacher_id

def test_get_course_by_id(test_client, test_db):
    # Assuming a course with ID 1 exists in the test setup
    response = test_client.get("/courses/1/")
    assert response.status_code == 200
    assert "name" in response.json()
    assert "teacher_id" in response.json()

def test_delete_course(test_client, test_db):
    # Assuming we have a course with ID 2 to delete
    response = test_client.delete("/courses/2/")
    assert response.status_code == 204

    # Verify that the course is deleted
    response = test_client.get("/courses/2/")
    assert response.status_code == 404
```