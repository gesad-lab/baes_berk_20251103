```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is in src/main.py

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_update_course_with_teacher(test_client):
    """Test updating a course with a valid teacher ID."""
    response = test_client.put("/courses/1", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_update_course_invalid_teacher(test_client):
    """Test updating a course with an invalid teacher ID."""
    response = test_client.put("/courses/1", json={"teacher_id": 999})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid teacher ID provided."}}

def test_get_course_with_teacher(test_client):
    """Test retrieving course details including teacher information."""
    response = test_client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["teacher_id"] is not None

def test_get_course_not_found(test_client):
    """Test retrieving a course that does not exist."""
    response = test_client.get("/courses/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Course not found."}}
```