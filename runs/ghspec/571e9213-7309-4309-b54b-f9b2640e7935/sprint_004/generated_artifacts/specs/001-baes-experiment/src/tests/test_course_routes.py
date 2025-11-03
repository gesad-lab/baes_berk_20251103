```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py
from models import Course, Student  # Assuming your Course and Student models are defined here
from sqlalchemy.exc import IntegrityError

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to set up and tear down the database for integration tests.
    This should create a fresh database before tests and drop it after.
    """
    # Code to set up the database (e.g., create necessary tables) would go here
    yield
    # Code to tear down the database would go here

def test_associate_course_with_student(setup_database):
    """
    Test to associate a course with a student using the POST API endpoint.
    """
    # Sample data (assume these exist in the database)
    student_id = 1
    course_id = 1

    response = client.post(f"/students/{student_id}/courses", json={"course_id": course_id})

    assert response.status_code == 200
    assert response.json() == {"message": "Course associated successfully"}

def test_retrieve_students_courses(setup_database):
    """
    Test to retrieve all courses associated with a student using the GET API endpoint.
    """
    student_id = 1

    response = client.get(f"/students/{student_id}/courses")

    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of courses
    assert len(response.json()) > 0  # Assuming there are courses associated

def test_remove_course_from_student(setup_database):
    """
    Test to remove a course association from a student using the DELETE API endpoint.
    """
    student_id = 1
    course_id = 1

    response = client.delete(f"/students/{student_id}/courses/{course_id}")

    assert response.status_code == 200
    assert response.json() == {"message": "Course removed successfully"}

def test_error_handling_invalid_course_association(setup_database):
    """
    Test to handle error when attempting to associate a nonexistent course with a student.
    """
    student_id = 1
    invalid_course_id = 9999  # Assuming this course does not exist

    response = client.post(f"/students/{student_id}/courses", json={"course_id": invalid_course_id})

    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Course does not exist"}}
```