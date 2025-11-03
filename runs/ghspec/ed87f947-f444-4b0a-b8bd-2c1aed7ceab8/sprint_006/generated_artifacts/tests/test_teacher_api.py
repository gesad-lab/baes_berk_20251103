```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py

@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

def test_assign_teacher_to_course(client):
    """Test assigning a teacher to a course successfully."""
    # Assuming a course exists with ID 1 and a teacher exists with ID 1
    response = client.post("/courses/1/assignTeacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully."}

def test_get_course_details_including_teacher(client):
    """Test retrieving course details including assigned teacher information."""
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()  # Check if teacher information is included
    assert response.json()["teacher"]["id"] == 1  # Verify that the assigned teacher's ID is correct

def test_update_teacher_assignment(client):
    """Test updating the teacher assignment for a course successfully."""
    response = client.put("/courses/1/assignTeacher", json={"teacher_id": 2})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assignment updated successfully."}

def test_assign_teacher_to_nonexistent_course(client):
    """Test assigning a teacher to a nonexistent course should fail."""
    response = client.post("/courses/999/assignTeacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found."}}

def test_assign_teacher_with_invalid_data(client):
    """Test invalid data when assigning a teacher should fail."""
    response = client.post("/courses/1/assignTeacher", json={"teacher_id": "invalid_id"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E400", "message": "Invalid teacher ID."}}
```