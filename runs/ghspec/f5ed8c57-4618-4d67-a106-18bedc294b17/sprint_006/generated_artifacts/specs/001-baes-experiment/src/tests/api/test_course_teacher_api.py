```python
import pytest
from fastapi.testclient import TestClient
from src.api.course_teacher_api import app  # Assuming FastAPI instance for course-teacher management
from src.models import Course  # Importing the Course model to interact with the database

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
    response = client.delete("/courses/1/remove_teacher")
    
    # Verify the DELETE request was successful
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher removed successfully from course."

    # Optionally verify that the teacher is actually removed from the course
    get_response = client.get("/courses/1")
    assert response.status_code == 200
    assert get_response.json()["teacher"] is None  # Assuming it should be None if no teacher is assigned
```