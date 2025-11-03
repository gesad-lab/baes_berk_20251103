```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.database import init_db, get_db
from src.models.enrollment import Enrollment
from sqlalchemy.orm import Session
from src.schemas.enrollment import EnrollmentCreate
from fastapi import HTTPException

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def db_session():
    # Initialize the database and create tables if necessary
    db = next(get_db())
    init_db()  # Ensure the database is initialized
    yield db
    # Teardown (cleanup) after tests
    db.rollback()
    db.close()

def test_enroll_student_in_course(test_client, db_session):
    """
    Test that a student can be enrolled in a course successfully. 
    This tests the endpoint: POST /students/{id}/enroll
    """
    # Given: An existing student and course
    student_id = 1
    course_id = 1
    enrollment_data = {"course_id": course_id}

    # When: Enrolling the student in the course
    response = test_client.post(f"/students/{student_id}/enroll", json=enrollment_data)

    # Then: Expect a successful response
    assert response.status_code == 200
    assert response.json() == {"message": "Student enrolled successfully", "enrollment_id": response.json()["enrollment_id"]}

def test_get_student_courses(test_client, db_session):
    """
    Test retrieval of all courses a student is enrolled in. 
    This tests the endpoint: GET /students/{id}/courses
    """
    student_id = 1

    response = test_client.get(f"/students/{student_id}/courses")

    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of courses

def test_deenroll_student_from_course(test_client, db_session):
    """
    Test that a student can be de-enrolled from a specific course successfully. 
    This tests the endpoint: DELETE /students/{studentId}/courses/{courseId}
    """
    student_id = 1
    course_id = 1

    response = test_client.delete(f"/students/{student_id}/courses/{course_id}")

    assert response.status_code == 200
    assert response.json() == {"message": "Student de-enrolled successfully"}
```