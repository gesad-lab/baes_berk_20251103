```python
import pytest
from fastapi.testclient import TestClient
from src.api.course_teacher_api import app  # Assuming FastAPI instance for course-teacher management is here

client = TestClient(app)

def test_assign_teacher_to_course():
    response = client.post(f"/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 201
    assert "course_id" in response.json()
    assert "teacher_id" in response.json()

def test_retrieve_course_with_teacher():
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()

def test_update_course_teacher():
    response = client.put("/courses/1/update_teacher", json={"teacher_id": 2})
    assert response.status_code == 200
    assert response.json()["new_teacher"]["id"] == 2

def test_remove_teacher_from_course():
    """Test removing a teacher from the course successfully."""
    response = client.delete("/courses/1/remove_teacher")
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher removed successfully from course."

def test_remove_teacher_from_nonexistent_course():
    """Test removing a teacher from a nonexistent course returns a 404 error."""
    response = client.delete("/courses/999/remove_teacher")
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E404"
    assert response.json()["error"]["message"] == "Course not found."

def test_remove_teacher_when_no_teacher_assigned():
    """Test removing a teacher from a course that has no assigned teacher."""
    response = client.delete("/courses/2/remove_teacher")  # Assuming course 2 has no assigned teacher
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E400"
    assert response.json()["error"]["message"] == "No teacher is currently assigned to this course."
```