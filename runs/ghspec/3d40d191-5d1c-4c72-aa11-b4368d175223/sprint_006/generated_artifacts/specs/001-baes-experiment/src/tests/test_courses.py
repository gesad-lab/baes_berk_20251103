```python
import pytest
from fastapi.testclient import TestClient
from src.api import app  # Import your FastAPI app instance

@pytest.fixture()
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)

def test_assign_teacher(client):
    """Test assigning a teacher to a course successfully."""
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})  # Sample course ID and teacher ID
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1  # Ensure the correct teacher ID is returned

def test_get_course_detail_with_teacher(client):
    """Test retrieving course details when a teacher is assigned."""
    response = client.get("/courses/1")  # Assume course 1 has an assigned teacher
    assert response.status_code == 200
    # Check if the teacher details are included
    assert response.json()["teacher"]["id"] is not None
    assert response.json()["teacher"]["name"] is not None  # Ensure Teacher's name is available

def test_get_course_detail_without_teacher(client):
    """Test retrieving course details when no teacher is assigned."""
    response = client.get("/courses/2")  # Assume course 2 has no assigned teacher
    assert response.status_code == 404
    assert response.json()["detail"] == "No Teacher assigned to this Course"
```