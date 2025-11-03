```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_enroll_student_success():
    """Test successful enrollment of a student in a course."""
    response = client.post("/students/1/enroll", json={"course_id": 1})
    assert response.status_code == 200
    assert response.json().get("message") == "Student enrolled in course successfully"

def test_enroll_nonexistent_student_fails():
    """Test enrollment failure when the student does not exist."""
    response = client.post("/students/999/enroll", json={"course_id": 1})
    assert response.status_code == 404
    assert "error" in response.json()

def test_retrieve_students_courses_success():
    """Test retrieval of courses for a valid student."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of course details

def test_retrieve_courses_nonexistent_student_fails():
    """Test failure when retrieving courses for a student that does not exist."""
    response = client.get("/students/999/courses")
    assert response.status_code == 404
    assert "error" in response.json()

def test_remove_student_from_course_success():
    """Test successful removal of a student from a course."""
    response = client.delete("/students/1/remove", json={"course_id": 1})
    assert response.status_code == 200
    assert response.json().get("message") == "Student removed from course successfully"

def test_remove_student_nonexistent_course_fails():
    """Test failure when trying to remove a student from a course that does not exist."""
    response = client.delete("/students/1/remove", json={"course_id": 999})
    assert response.status_code == 404
    assert "error" in response.json()
```