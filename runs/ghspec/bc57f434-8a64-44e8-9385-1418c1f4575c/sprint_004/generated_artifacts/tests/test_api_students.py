```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is in src/main.py

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_enroll_student_in_course(test_client):
    """Test enrolling a student in a course."""
    response = test_client.post("/students/1/enroll", json={"course_id": 1})
    assert response.status_code == 201
    assert response.json() == {"message": "Enrollment successful."}

def test_get_student_courses(test_client):
    """Test retrieving courses for a specific student."""
    response = test_client.get("/students/1/courses")
    assert response.status_code == 200
    assert response.json() == {"courses": [1, 2]}  # Example output

def test_enroll_student_with_invalid_ids(test_client):
    """Test enrollment with invalid student or course ID."""
    
    # Test with non-existent student ID
    response = test_client.post("/students/999/enroll", json={"course_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student or Course not found."}}

    # Test with invalid course ID
    response = test_client.post("/students/1/enroll", json={"course_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student or Course not found."}}

    # Test without student ID
    response = test_client.post("/students//enroll", json={"course_id": 1})  # Invalid student ID
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid student ID provided."}}

    # Test without course ID
    response = test_client.post("/students/1/enroll", json={})  # Missing course ID
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Course ID is required."}}
```