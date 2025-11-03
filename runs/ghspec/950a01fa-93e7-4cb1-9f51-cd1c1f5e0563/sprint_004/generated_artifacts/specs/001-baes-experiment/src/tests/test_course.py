import pytest
from fastapi.testclient import TestClient
from src.main import app  # FastAPI app
from src.db import init_db, shutdown_db  # Database management functions
from src.models import Course, Student, Enrollment  # Assuming you have these models

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Set up the database for testing."""
    init_db()
    yield
    shutdown_db()

@pytest.fixture
def client():
    """Create a TestClient for FastAPI app."""
    return TestClient(app)

def test_enroll_student_in_course(client):
    """Test enrolling a student in a course."""
    # Create a course and student for testing
    course_response = client.post("/courses/", json={"name": "Mathematics", "level": "Beginner"})
    student_response = client.post("/students/", json={"name": "John Doe"})

    assert course_response.status_code == 201
    assert student_response.status_code == 201

    course_id = course_response.json()["id"]
    student_id = student_response.json()["id"]

    # Enroll student in the course
    enrollment_response = client.post(f"/enrollments/", json={"student_id": student_id, "course_id": course_id})

    assert enrollment_response.status_code == 200
    assert enrollment_response.json() == {"message": "Enrollment successful"}

def test_retrieve_student_courses(client):
    """Test retrieving all courses associated with a specific student."""
    # Assume the student and course have already been created and student is enrolled
    student_response = client.post("/students/", json={"name": "Jane Smith"})
    assert student_response.status_code == 201

    student_id = student_response.json()["id"]

    course_response = client.post("/courses/", json={"name": "Science", "level": "Intermediate"})
    assert course_response.status_code == 201
    course_id = course_response.json()["id"]

    # Enroll student in the course
    client.post(f"/enrollments/", json={"student_id": student_id, "course_id": course_id})

    # Retrieve courses for the student
    courses_response = client.get(f"/students/{student_id}/courses/")
    
    assert courses_response.status_code == 200
    assert len(courses_response.json()) == 1
    assert courses_response.json()[0]["name"] == "Science"

def test_enroll_student_with_invalid_course_id(client):
    """Test enrolling a student with an invalid course ID."""
    student_response = client.post("/students/", json={"name": "Alice Johnson"})
    assert student_response.status_code == 201
    student_id = student_response.json()["id"]

    # Attempt to enroll student using an invalid course ID
    invalid_enrollment_response = client.post(f"/enrollments/", json={"student_id": student_id, "course_id": 999})

    assert invalid_enrollment_response.status_code == 400
    assert invalid_enrollment_response.json() == {"error": {"code": "E001", "message": "Invalid course ID"}}  

def test_error_handling_for_unenrollment(client):
    """Test error handling when unenrolling a student from a course they are not enrolled in."""
    student_response = client.post("/students/", json={"name": "Bob Williams"})
    assert student_response.status_code == 201
    student_id = student_response.json()["id"]

    course_response = client.post("/courses/", json={"name": "History", "level": "Advanced"})
    assert course_response.status_code == 201
    course_id = course_response.json()["id"]

    # Attempt to unenroll without enrolling
    unenrollment_response = client.delete(f"/enrollments/", json={"student_id": student_id, "course_id": course_id})
    
    assert unenrollment_response.status_code == 404
    assert unenrollment_response.json() == {"error": {"code": "E002", "message": "Student is not enrolled in the specified course"}}