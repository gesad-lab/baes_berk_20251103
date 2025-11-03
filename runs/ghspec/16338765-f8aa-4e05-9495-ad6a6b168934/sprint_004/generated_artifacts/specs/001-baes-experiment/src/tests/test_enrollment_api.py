```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust the import based on your actual project structure
from src.models import Course, Student, StudentCourse  # Import necessary data models

client = TestClient(app)

# Test enrollment of a student in a course
def test_enroll_student_in_course():
    response = client.post("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 201
    data = response.json()
    assert data["student_id"] == 1
    assert data["course_id"] == 1

# Test retrieval of courses for a student
def test_get_courses_for_student():
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["courses"], list)  # Ensure we get a list back

# Test updating courses for a student
def test_update_courses_for_student():
    response = client.put("/students/1/courses", json={"course_ids": [1, 2]})
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == 1
    assert sorted(data["course_ids"]) == sorted([1, 2])
```