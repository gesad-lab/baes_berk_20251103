```python
import pytest
from fastapi.testclient import TestClient
from api.enrollment import app  # Assuming the FastAPI app is defined in api/enrollment.py
from models.enrollment import CourseEnrollment, EnrolledCoursesResponse  # Import necessary models
from database import get_student_courses, enroll_student, get_students_enrolled_in_course  # Import database functions or ORM methods

client = TestClient(app)

# Assuming you have a test database setup for the test cases

@pytest.fixture
def setup_database():
    # Setup code to initialize a test database, create necessary entries for students and courses
    pass  # Implement as per your testing strategy

@pytest.mark.usefixtures("setup_database")
def test_enroll_student():
    """Test enrolling a student in a course successfully."""
    student_id = 1  # Use a valid student ID from your test setup
    course_id = 10  # Use a valid course ID from your test setup
    enrollment_data = CourseEnrollment(course_id=course_id)

    response = client.post(f"/students/{student_id}/courses", json=enrollment_data.dict())
    assert response.status_code == 200  # Adjust according to your implementation
    assert response.json() == {"message": "Enrollment successful"}  # Adjust to expected response structure

def test_view_courses_for_student():
    """Test viewing courses for a specific student."""
    student_id = 1  # Use a valid student ID from your test setup
    response = client.get(f"/students/{student_id}/courses")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of courses
    assert len(response.json()) > 0  # Ensure there are courses returned

def test_enroll_student_with_invalid_course_id():
    """Test enrolling a student with an invalid course ID."""
    student_id = 1  # Use a valid student ID from your test setup
    invalid_course_id = 999  # Assuming this ID does not exist
    enrollment_data = CourseEnrollment(course_id=invalid_course_id)

    response = client.post(f"/students/{student_id}/courses", json=enrollment_data.dict())
    assert response.status_code == 404  # Expected 404 for non-existent course
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}  # Adjust to response format

def test_list_students_by_course():
    """Test listing students by specific course ID."""
    course_id = 10  # Use a valid course ID from your test setup
    response = client.get(f"/courses/{course_id}/students")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of students
    assert len(response.json()) > 0  # Ensure there are students returned
```