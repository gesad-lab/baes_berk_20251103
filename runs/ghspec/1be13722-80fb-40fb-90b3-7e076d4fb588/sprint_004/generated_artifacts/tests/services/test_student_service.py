```python
from fastapi.testclient import TestClient
import pytest
from src.api.student import app  # Assuming this is where the FastAPI app instance is defined
from models.student import Student  # Assuming Student is defined in models
from models.course import Course  # Assuming Course is defined in models
from sqlalchemy.orm import Session

client = TestClient(app)

# Mock database session fixture (setup and teardown as needed)
@pytest.fixture(scope="module")
def db_session():
    # Logic to create a database session and clean up afterward
    # This is a placeholder ...
    yield  # Replace with proper session management
    # Clean up logic goes here

def test_associate_student_with_course_success(db_session):
    """Test successful association of a course to a student."""
    student_id = 1  # Assume a valid student ID exists
    course_id = 101  # Assume a valid course ID exists
    response = client.patch(f"/students/{student_id}/courses", json={"course_id": course_id})
    
    assert response.status_code == 200
    assert response.json() == {"message": "Course associated successfully"}

def test_retrieve_student_courses_success(db_session):
    """Test retrieval of courses associated with a student."""
    student_id = 1  # Assume a valid student ID exists
    response = client.get(f"/students/{student_id}/courses")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of courses
    # Additional checks can be done on the content of the list

def test_associate_student_with_nonexistent_course(db_session):
    """Test handling of a nonexistent course association."""
    student_id = 1  # Assume a valid student ID exists
    invalid_course_id = 9999  # Assume this course doesn't exist
    response = client.patch(f"/students/{student_id}/courses", json={"course_id": invalid_course_id})
    
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid course ID", "details": {}}}
```