```python
import pytest
from fastapi.testclient import TestClient
from myapp.main import app  # Assuming that the FastAPI app is defined in myapp/main.py
from myapp.database import create_database_schema, get_session
from myapp.models import Course, StudentCourses  # Assuming you have Course and StudentCourses models defined

# Create a TestClient for making requests to the FastAPI app
client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Fixture to set up the database schema on startup."""
    create_database_schema()  # Create the initial database schema
    yield  # This allows tests to run
    # Logic to tear down the database could go here if needed

def test_enroll_student():
    """Test enrolling a student in a course."""
    student_id = 1  # Example student ID
    course_id = 1   # Example course ID

    # Attempt to enroll the student in the course
    response = client.post(f"/students/{student_id}/enroll", json={"course_id": course_id})
    
    # Validate successful enrollment
    assert response.status_code == 200
    assert response.json() == {"message": "Student enrolled successfully"}

def test_get_student_courses():
    """Test retrieving enrolled courses for a student."""
    student_id = 1  # Example student ID

    # Retrieve the courses for the student
    response = client.get(f"/students/{student_id}/courses")
    
    # Validate the response
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of courses
    # Add additional assertions based on expected course data
```