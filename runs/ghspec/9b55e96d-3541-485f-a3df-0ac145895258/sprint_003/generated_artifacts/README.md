```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_course_success():
    response = client.post("/courses", json={"name": "Mathematics 101", "level": "Beginner"})
    assert response.status_code == 200
    assert response.json().get("message") == "Course created successfully"

def test_create_course_without_required_fields_fails():
    response = client.post("/courses", json={"name": ""})
    assert response.status_code == 400
    assert "error" in response.json()

def test_create_course_without_level_field_fails():
    response = client.post("/courses", json={"name": "Biology 102"})
    assert response.status_code == 400
    assert "error" in response.json()

def test_retrieve_course_success():
    # Create a course first
    create_response = client.post("/courses", json={"name": "Physics 101", "level": "Beginner"})
    assert create_response.status_code == 200
    
    # Now retrieve the created course
    course_id = create_response.json().get("id")
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Physics 101"
    assert response.json()["level"] == "Beginner"

def test_retrieve_nonexistent_course_fails():
    response = client.get("/courses/999999")  # Non-existent course ID
    assert response.status_code == 404
    assert "error" in response.json()
```