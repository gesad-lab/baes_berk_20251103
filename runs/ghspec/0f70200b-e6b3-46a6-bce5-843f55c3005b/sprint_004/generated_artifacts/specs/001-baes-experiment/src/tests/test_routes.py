```python
import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.models import Course

client = TestClient(app)

@pytest.fixture(scope="module")
def test_courses():
    """Setup test courses in the database before any tests run."""
    # Assume a setup function exists to clear and populate the database
    clear_and_seed_database_with_courses()
    yield
    # Tear down test database cleanup
    clear_test_database()

def test_create_course_success():
    """Test successful creation of a new course."""
    response = client.post("/courses", json={"name": "Test Course"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Course"

def test_enroll_student_success():
    """Test enrolling a student in a course successfully."""
    response = client.post("/students/1/enroll", json={"course_id": 1})
    assert response.status_code == 201
    # Further checks can include verifying course enrollment in the database.

def test_enroll_student_invalid_course():
    """Test enrolling a student with an invalid course ID."""
    response = client.post("/students/1/enroll", json={"course_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}

def test_get_student_courses():
    """Test retrieving a list of courses a student is enrolled in."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list
    # Further checks for the actual content can be added based on the test data

def test_enroll_student_duplicate():
    """Test enrolling a student in the same course twice."""
    response = client.post("/students/1/enroll", json={"course_id": 1})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E400", "message": "Student is already enrolled in this course"}}
```