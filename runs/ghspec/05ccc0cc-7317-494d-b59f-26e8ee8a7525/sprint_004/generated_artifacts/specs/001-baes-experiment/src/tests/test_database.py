```python
# tests/test_database.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Course, Enrollment  # Import the new Enrollment model
from app.database import engine

# Set up the test database
@pytest.fixture(scope="module")
def test_db():
    # Create the database schema, including the Course and Enrollment tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests are done
    Base.metadata.drop_all(bind=engine)

# Test client instance for making API requests
@pytest.fixture(scope='module')
def client():
    with TestClient(app) as test_client:
        yield test_client

# Test case for enrolling a student in a course
def test_enroll_student(client):
    # Sample data for the test
    student_id = 1  # Assume this student already exists
    course_id = 1   # Assume this course already exists
    
    # Enroll the student in the course
    response = client.post(f"/students/{student_id}/enroll", json={"course_id": course_id})

    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    # Assert that the response includes updated student details
    assert "student_id" in response.json()

# Test case for retrieving student details with enrolled courses
def test_get_student_with_courses(client):
    student_id = 1  # Assume this student already exists
    response = client.get(f"/students/{student_id}")

    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    # Assert that the response includes student details and an array of courses
    assert "courses" in response.json()

# Test case for error handling when trying to enroll in an invalid course
def test_enroll_student_invalid_course(client):
    student_id = 1  # Assume this student already exists
    invalid_course_id = 999  # Assume this course does not exist
    
    # Attempt to enroll the student in an invalid course
    response = client.post(f"/students/{student_id}/enroll", json={"course_id": invalid_course_id})

    # Assert that the response status code indicates an error
    assert response.status_code == 400
    # Assert that the error message is appropriate
    assert response.json() == {"error": {"code": "E001", "message": "Invalid course specified."}}
```