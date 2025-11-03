```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Student, Course, Enrollment
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
    with TestClient(app) as c:
        yield c

def test_enroll_student_in_course(client):
    # Pre-requisite: create a student and a course for testing
    student_data = {"name": "John Doe"}
    course_data = {"title": "Math 101"}

    # Create a student
    response = client.post("/students", json=student_data)
    assert response.status_code == 201
    student_id = response.json()["id"]

    # Create a course
    response = client.post("/courses", json=course_data)
    assert response.status_code == 201
    course_id = response.json()["id"]

    # Enroll the student in the course
    enrollment_response = client.post(f"/enrollments", json={"student_id": student_id, "course_id": course_id})
    assert enrollment_response.status_code == 200
    assert enrollment_response.json()["student_id"] == student_id
    assert enrollment_response.json()["course_id"] == course_id

def test_retrieve_student_details_with_courses(client):
    student_data = {"name": "Jane Doe"}
    response = client.post("/students", json=student_data)
    assert response.status_code == 201
    student_id = response.json()["id"]

    course_data = {"title": "Science 101"}
    response = client.post("/courses", json=course_data)
    assert response.status_code == 201
    course_id = response.json()["id"]

    client.post("/enrollments", json={"student_id": student_id, "course_id": course_id})

    # Retrieve student details
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert "courses" in response.json()

def test_error_handling_invalid_enrollment(client):
    invalid_course_id = 999  # Assuming this course ID does not exist
    student_data = {"name": "Alice Smith"}

    # Create a student
    response = client.post("/students", json=student_data)
    assert response.status_code == 201
    student_id = response.json()["id"]

    # Attempt to enroll the student in an invalid course
    enrollment_response = client.post(f"/enrollments", json={"student_id": student_id, "course_id": invalid_course_id})
    assert enrollment_response.status_code == 404  # Expecting Not Found for invalid course ID
    assert enrollment_response.json() == {"error": {"code": "E001", "message": "Invalid course ID.", "details": {}}}
```