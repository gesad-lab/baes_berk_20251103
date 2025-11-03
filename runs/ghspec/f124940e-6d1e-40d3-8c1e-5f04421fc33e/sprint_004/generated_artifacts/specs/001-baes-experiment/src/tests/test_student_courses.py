```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is instantiated in src/main.py
from src.models import Course  # Import the Course model for testing
from src.services.student_course_service import enroll_student  # Import the enroll function for validation

client = TestClient(app)

@pytest.fixture(scope="module")
def create_course():
    # Setup: Create a course in the database for testing
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    yield response.json()
    # Teardown: Cleanup created course
    client.delete(f"/courses/{response['id']}")

def test_enroll_student(create_course):
    response = client.post("/students/1/enroll", json={"course_id": create_course["id"]})
    assert response.status_code == 200
    assert response.json()["enrolled_courses"][0]["course_id"] == create_course["id"]

def test_enroll_student_invalid_course():
    # Trying to enroll in a non-existent course
    response = client.post("/students/1/enroll", json={"course_id": 999})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Course not found."}}

def test_get_student_courses():
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure it's a list

def test_remove_course_from_enrollment(create_course):
    # First, enroll in the course
    client.post("/students/1/enroll", json={"course_id": create_course["id"]})
    
    response = client.delete(f"/students/1/enroll/{create_course['id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Course removed successfully"
```