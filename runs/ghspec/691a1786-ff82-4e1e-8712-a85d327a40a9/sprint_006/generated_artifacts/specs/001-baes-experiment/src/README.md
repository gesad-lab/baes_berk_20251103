```python
# File: tests/test_course.py

import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.teacher import Teacher
from src.models.course import Course
from src.db.database import get_db
from sqlalchemy.orm import Session
from src.schemas.course_schemas import CourseCreate, CourseUpdate

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def test_db():
    # Setup code for initializing the database
    pass

@pytest.fixture(scope="module")
def create_dummy_teacher(test_db):
    # Create a dummy teacher for testing
    teacher = Teacher(name="Test Teacher")
    test_db.add(teacher)
    test_db.commit()
    test_db.refresh(teacher)
    return teacher

@pytest.fixture(scope="module")
def create_dummy_course(test_db, create_dummy_teacher):
    # Create a dummy course for testing
    course = Course(name="Test Course", teacher_id=create_dummy_teacher.id)
    test_db.add(course)
    test_db.commit()
    test_db.refresh(course)
    return course

def test_create_course(test_client, create_dummy_teacher):
    course_data = CourseCreate(name="New Course", teacher_id=create_dummy_teacher.id)
    response = test_client.post("/courses/", json=course_data.dict())
    assert response.status_code == 201
    assert response.json()["name"] == course_data.name
    assert response.json()["teacher_id"] == create_dummy_teacher.id

def test_get_course(test_client, create_dummy_course):
    response = test_client.get(f"/courses/{create_dummy_course.id}")
    assert response.status_code == 200
    assert response.json()["id"] == create_dummy_course.id
    assert response.json()["name"] == create_dummy_course.name

def test_update_course(test_client, create_dummy_course):
    update_data = CourseUpdate(name="Updated Course Name")
    response = test_client.put(f"/courses/{create_dummy_course.id}", json=update_data.dict())
    assert response.status_code == 200
    assert response.json()["name"] == update_data.name

def test_delete_course(test_client, create_dummy_course):
    response = test_client.delete(f"/courses/{create_dummy_course.id}")
    assert response.status_code == 204  # No Content
    # Check if course no longer exists
    response = test_client.get(f"/courses/{create_dummy_course.id}")
    assert response.status_code == 404  # Not Found
```