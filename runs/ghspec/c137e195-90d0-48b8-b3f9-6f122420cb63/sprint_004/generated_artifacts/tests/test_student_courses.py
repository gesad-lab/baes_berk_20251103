```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from api.student_courses import router as student_course_router
from models.student_course_association import StudentCourseAssociation
from database.db import init_db

# Set up FastAPI app for testing
app = FastAPI()
app.include_router(student_course_router)

@pytest.fixture(scope="module")
def client():
    """Create a test client for the FastAPI app."""
    init_db()  # Initialize the database
    yield TestClient(app)  # Provide the test client to the tests

def test_assign_course_to_student_success(client):
    """Test assigning a valid course to a student."""
    response = client.post("/assign_course", json={"student_id": 1, "course_id": 1})
    assert response.status_code == 200  # Expecting a 200 OK status
    data = response.json()
    assert data["student_id"] == 1
    assert 1 in [course["id"] for course in data["courses"]]

def test_retrieve_student_with_courses_success(client):
    """Test that retrieving student data includes their courses."""
    response = client.get("/students/1")
    assert response.status_code == 200  # Expecting a 200 OK status
    data = response.json()
    assert data["id"] == 1
    assert isinstance(data["courses"], list)  # Courses should be a list

def test_assign_non_existent_course(client):
    """Test assigning a non-existent course returns an error."""
    response = client.post("/assign_course", json={"student_id": 1, "course_id": 999})
    assert response.status_code == 404  # Expecting a 404 Not Found status
    data = response.json()
    assert data == {
        "error": {
            "code": "E404",
            "message": "Course not found",
            "details": {}
        }
    }

def test_assign_course_to_non_existent_student(client):
    """Test assigning a course to a non-existent student returns an error."""
    response = client.post("/assign_course", json={"student_id": 999, "course_id": 1})
    assert response.status_code == 404  # Expecting a 404 Not Found status
    data = response.json()
    assert data == {
        "error": {
            "code": "E404",
            "message": "Student not found",
            "details": {}
        }
    }
```