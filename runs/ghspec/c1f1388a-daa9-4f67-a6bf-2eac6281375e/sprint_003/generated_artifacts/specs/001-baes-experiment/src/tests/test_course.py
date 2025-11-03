```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.database import init_db, get_db
from src.models.course import Course
from sqlalchemy.orm import Session
from src.schemas.course import CourseCreate
from fastapi import HTTPException

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def db_session():
    # Initialize the database and create tables if needed
    db = next(get_db())
    init_db()
    yield db  # Provides the session for tests
    # teardown code could go here to drop tables or clean up if necessary

def test_create_course_valid(db_session, test_client):
    """Test creating a course with valid data"""
    course_data = {"name": "Introduction to Programming", "level": "Beginner"}
    response = test_client.post("/courses/", json=course_data)
    assert response.status_code == 201
    assert "id" in response.json()  # Check if the course ID is returned
    assert response.json()["name"] == course_data["name"]
    assert response.json()["level"] == course_data["level"]

def test_create_course_missing_name(db_session, test_client):
    """Test error handling for missing required fields (course name)"""
    course_data = {"level": "Intermediate"}
    response = test_client.post("/courses/", json=course_data)
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "name"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

def test_create_course_missing_level(db_session, test_client):
    """Test error handling for missing required fields (course level)"""
    course_data = {"name": "Advanced Mathematics"}
    response = test_client.post("/courses/", json=course_data)
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "level"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

def test_retrieve_courses(db_session, test_client):
    """Test retrieval of courses"""
    response = test_client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of courses
    # Optionally, we could check if a known course appears in the list
```