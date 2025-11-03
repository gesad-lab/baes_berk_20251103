```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your main app is in a file called main.py
from models import Course  # Ensure you import the Course model 

client = TestClient(app)

# Test case for creating a new course
def test_create_course():
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json() == {"name": "Mathematics", "level": "Beginner"}

# Test case for retrieving the list of courses
def test_get_courses():
    response = client.get("/courses")
    assert response.status_code == 200
    # Ensure the response is a list and includes the correct attributes
    assert isinstance(response.json(), list)
    assert all("name" in course and "level" in course for course in response.json())

# Test case for creating a course without a name
def test_create_course_without_name():
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Course name is required."}}

# Test case for creating a course without a level
def test_create_course_without_level():
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Course level is required."}}

# Test case for creating a course with missing both fields
def test_create_course_without_fields():
    response = client.post("/courses", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E003", "message": "Course name and level are required."}}
```