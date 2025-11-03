```python
import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.models import Course, Student

client = TestClient(app)

@pytest.fixture(scope="module")
def test_courses():
    """Setup test courses in the database before any tests run."""
    clear_and_seed_database_with_courses()
    yield
    clear_test_database()

@pytest.fixture(scope="module")
def test_students():
    """Setup test students in the database before any tests run."""
    clear_and_seed_database_with_students()
    yield
    clear_test_database()

def test_fetch_student_courses_success(test_students):
    """Test fetching a student's enrolled courses successfully."""
    student_id = 1  # Assuming a student with ID 1 exists
    response = client.get(f"/students/{student_id}/courses")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure response is a list
    # Assuming there are courses for the student, and at least one exists
    assert len(response.json()) > 0

def test_fetch_student_courses_no_courses(test_students):
    """Test fetching a student's courses when none are enrolled."""
    student_id = 2  # Assuming student with ID 2 has no courses
    response = client.get(f"/students/{student_id}/courses")
    
    assert response.status_code == 200
    assert response.json() == []  # Should return an empty list

def test_fetch_courses_for_non_existent_student():
    """Test fetching courses for a non-existent student."""
    student_id = 9999  # Assuming no student with this ID exists
    response = client.get(f"/students/{student_id}/courses")
    
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found"}}
```