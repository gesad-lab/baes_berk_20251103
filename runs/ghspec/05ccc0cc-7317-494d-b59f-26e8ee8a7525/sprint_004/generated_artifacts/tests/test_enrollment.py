```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Enrollment, Student, Course
from app.database import engine

# Set up the test database for enrollment entity tests
@pytest.fixture(scope="module")
def test_db():
    # Create the database schema, including the Enrollment table
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests are done
    Base.metadata.drop_all(bind=engine)

# Test client instance for making API requests
@pytest.fixture(scope='module')
def client(test_db):
    # Return a test client instance
    return TestClient(app)

def test_enroll_student_in_course(client):
    # Test data
    student_id = 1
    course_id = 1

    # Assuming we have at least one student and one course to enroll
    response = client.post(f"/students/{student_id}/enroll", json={"course_id": course_id})

    # Validate the response for successful enrollment
    assert response.status_code == 200
    assert "student_id" in response.json()
    assert response.json()["student_id"] == student_id
    assert course_id in response.json()["courses"]

def test_retrieve_student_details_with_courses(client):
    student_id = 1

    # Retrieve student details
    response = client.get(f"/students/{student_id}")

    # Validate the response contains student details and courses
    assert response.status_code == 200
    assert "id" in response.json()
    assert "courses" in response.json()

def test_error_handling_invalid_enrollment(client):
    student_id = 1
    invalid_course_id = 99999  # Assuming this course ID does not exist

    # Attempt to enroll student in an invalid course
    response = client.post(f"/students/{student_id}/enroll", json={"course_id": invalid_course_id})

    # Validate the response for error handling
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid course ID"}} 
```