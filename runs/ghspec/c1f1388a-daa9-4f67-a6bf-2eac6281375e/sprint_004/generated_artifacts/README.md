```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.database import init_db, get_db
from src.models.student import Student
from src.models.course import Course
from sqlalchemy.orm import Session
from fastapi import HTTPException

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def db_session():
    # Initialize the database and create tables if needed
    pass

def test_enroll_non_existent_student(test_client):
    """Test enrolling a course for a non-existent student returns 404 error."""
    response = test_client.post("/students/999/enroll", json={"course_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found", "details": {}}}

def test_enroll_non_existent_course(test_client):
    """Test enrolling a student for a non-existent course returns 404 error."""
    response = test_client.post("/students/1/enroll", json={"course_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found", "details": {}}}

def test_enroll_student_in_course(test_client):
    """Test successful enrollment of an existing student in an existing course."""
    response = test_client.post("/students/1/enroll", json={"course_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Enrolled successfully"}

def test_retrieve_student_courses(test_client):
    """Test retrieving courses for a specific student."""
    response = test_client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Assuring the response is a list

def test_de_enroll_student_from_course(test_client):
    """Test successful de-enrollment of a student from a course."""
    response = test_client.delete("/students/1/de-enroll", json={"course_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully de-enrolled"}
```