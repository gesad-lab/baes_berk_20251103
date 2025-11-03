```python
import pytest
from fastapi.testclient import TestClient
from src.api.course_api import app  # Assuming the FastAPI instance for course is in this module
from src.database import get_db, Database  # Assuming there's a database module

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    # Create a new in-memory database or use a test database
    test_db = Database()
    test_db.create_tables()
    yield test_db
    test_db.drop_tables()

def test_list_courses_empty(db):
    # Test listing courses when no courses have been created
    response = client.get("/courses")
    assert response.status_code == 200
    assert response.json() == []  # Expecting an empty list

def test_create_course(db):
    # Create a new course and verify it exists in the list
    response = client.post("/courses", json={"name": "Introduction to Programming", "level": "Beginner"})
    assert response.status_code == 201
    created_course = response.json()
    assert created_course["id"] is not None
    assert created_course["name"] == "Introduction to Programming"
    assert created_course["level"] == "Beginner"

def test_list_courses_after_creation(db):
    # List courses after creating one course
    response = client.get("/courses")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) == 1
    assert courses[0]["name"] == "Introduction to Programming"
    assert courses[0]["level"] == "Beginner"

def test_create_course_duplicate(db):
    # Attempt to create a course with the same name and level and expect an error or logical response
    response = client.post("/courses", json={"name": "Introduction to Programming", "level": "Beginner"})
    assert response.status_code == 400  # Expecting a bad request due to duplicate

def test_list_courses_with_multiple_entries(db):
    # Create another course and check the list
    client.post("/courses", json={"name": "Data Structures", "level": "Intermediate"})
    
    response = client.get("/courses")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) == 2  # Expecting two courses now
    assert any(course["name"] == "Data Structures" for course in courses)
```