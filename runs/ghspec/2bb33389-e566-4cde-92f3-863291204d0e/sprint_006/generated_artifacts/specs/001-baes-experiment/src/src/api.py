```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import init_db, Base, SessionLocal
from src.models import Course, Teacher  # Assuming Teacher model is defined in src/models.py
from src.api import app  # Assuming the FastAPI app is defined in src/api

DATABASE_URL = "sqlite:///./test.db"

# Create a new database engine for testing
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a new FastAPI TestClient
@pytest.fixture(scope="module")
def client():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    # Initialize the database
    init_db()
    
    yield TestClient(app)
    
    # Drop all tables after testing
    Base.metadata.drop_all(bind=engine)

# Scenario 1: Assign a Teacher to a Course
def test_assign_teacher_to_course(client):
    # Assuming we have valid IDs 1 for course and 1 for teacher inserted in the test database
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned to course successfully."}

# Scenario 2: Assign a Teacher to a Non-Existent Course
def test_assign_teacher_to_non_existent_course(client):
    response = client.post("/courses/999/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E004", "message": "Course not found."}}

# Scenario 3: Assign Non-Existent Teacher to Course
def test_assign_non_existent_teacher_to_course(client):
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E005", "message": "Teacher not found."}}

# Scenario 4: Get Course with Assigned Teacher
def test_get_course_with_assigned_teacher(client):
    # Assuming we have a course with ID 1 that has a teacher assigned in the test database
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()
```