```python
# File: tests/test_students.py
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Course, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base

# Setup the test client
@pytest.fixture(scope="module")
def test_client():
    engine = create_engine("sqlite:///./test.db")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    with TestingSessionLocal() as session:
        # Create the database tables
        Base.metadata.create_all(bind=engine)
        
        # Insert test data
        course1 = Course(id="course-1", name="Course 1")
        course2 = Course(id="course-2", name="Course 2")
        student = Student(id="student-1", name="Student 1")
        
        session.add(course1)
        session.add(course2)
        session.add(student)
        session.commit()
        
    yield TestClient(app)

    # Cleanup
    with TestingSessionLocal() as session:
        Base.metadata.drop_all(bind=engine)

# Test: Check validation for invalid course IDs when linking courses to a student
def test_link_courses_with_invalid_ids(test_client):
    response = test_client.patch(
        "/students/student-1",
        json={"courses": ["invalid-course-id", "another-invalid-id"]}
    )
    
    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400
    
    # Check if the response contains the appropriate validation error message
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Invalid course IDs provided.",
            "details": {
                "invalid_ids": ["invalid-course-id", "another-invalid-id"]
            }
        }
    }

# Test: Check for valid course IDs
def test_link_courses_with_valid_ids(test_client):
    response = test_client.patch(
        "/students/student-1",
        json={"courses": ["course-1", "course-2"]}
    )
    
    # Assert that the response status code is 200 (OK) and the student is updated correctly
    assert response.status_code == 200
    updated_student = response.json()
    assert updated_student['id'] == "student-1"
    assert sorted(updated_student['courses']) == sorted(["course-1", "course-2"])
```