```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import init_db, Base, SessionLocal
from src.models import Course, Student, Teacher  # Assuming Teacher model is defined in src/models.py
from src.api import app  # Assuming the FastAPI app is defined in src/api

DATABASE_URL = "sqlite:///./test.db"

# Create a new database engine for testing
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Test Client
@pytest.fixture(scope="module")
def client():
    # Setup: Create the database and tables
    Base.metadata.create_all(bind=engine)
    init_db()

    with TestClient(app) as c:
        yield c

    # Teardown: Drop the database after tests
    Base.metadata.drop_all(bind=engine)

# Test assigning a teacher to a course successfully
def test_assign_teacher_to_course(client):
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned to course successfully."}

# Test assigning a teacher to a non-existent course
def test_assign_teacher_to_non_existent_course(client):
    response = client.post("/courses/999/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E004", "message": "Course not found."}}

# Test assigning a non-existent teacher to a course
def test_assign_non_existent_teacher_to_course(client):
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E005", "message": "Teacher not found."}}

# Test retrieving a course with an assigned teacher
def test_get_course_with_assigned_teacher(client):
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()
```