```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_associate_courses_with_valid_data(client):
    """Test associating courses with a student."""
    response = client.post("/students/1/courses", json={"course_ids": [1, 2, 3]})
    assert response.status_code == 200  # 200 OK
    assert response.json() == {"message": "Courses associated successfully with the student."}

def test_get_student_courses(client):
    """Test retrieving a student's courses."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200  # 200 OK
    assert isinstance(response.json(), list)  # Ensure response is a list

def test_associate_courses_with_invalid_student(client):
    """Test associating courses with a nonexistent student."""
    response = client.post("/students/999/courses", json={"course_ids": [1, 2]})
    assert response.status_code == 404  # 404 Not Found
    assert response.json() == {"error": {"code": "E404", "message": "Student not found."}}

def test_associate_nonexistent_courses(client):
    """Test trying to associate a nonexistent course with a student."""
    response = client.post("/students/1/courses", json={"course_ids": [999]})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {"error": {"code": "E400", "message": "Invalid course IDs provided."}}

def test_get_courses_for_nonexistent_student(client):
    """Test retrieving courses for a nonexistent student."""
    response = client.get("/students/999/courses")
    assert response.status_code == 404  # 404 Not Found
    assert response.json() == {"error": {"code": "E404", "message": "Student not found."}}

```