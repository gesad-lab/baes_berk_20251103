```python
# tests/test_courses.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_enroll_student_with_invalid_student_id():
    """Test enrolling a student with an invalid student ID."""
    response = client.post("/students/invalid_student_id/courses", json={"course_id": "valid_course_id"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid student ID or course ID"}}

def test_enroll_student_with_invalid_course_id():
    """Test enrolling a student with an invalid course ID."""
    response = client.post("/students/valid_student_id/courses", json={"course_id": "invalid_course_id"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid student ID or course ID"}}

def test_enroll_student_without_student_id():
    """Test enrolling a student without providing a student ID."""
    response = client.post("/students//courses", json={"course_id": "valid_course_id"})
    assert response.status_code == 422  # Unprocessable Entity for missing required fields.

def test_enroll_student_without_course_id():
    """Test enrolling a student without providing a course ID."""
    response = client.post("/students/valid_student_id/courses", json={})
    assert response.status_code == 422  # Unprocessable Entity for missing required fields.
```