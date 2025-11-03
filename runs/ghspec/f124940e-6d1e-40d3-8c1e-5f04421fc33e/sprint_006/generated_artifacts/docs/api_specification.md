import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming FastAPI app is instantiated in src/main.py

client = TestClient(app)

def test_assign_teacher():
    """Test assigning a valid teacher to a course."""
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["teacher"]["id"] == 1

def test_get_course_with_teacher():
    """Test retrieving course details with assigned teacher."""
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["teacher"]["id"] == 1

def test_unassign_teacher():
    """Test unassigning a teacher from a course."""
    response = client.delete("/courses/1/unassign_teacher")
    assert response.status_code == 200
    assert response.json()["teacher"] is None

def test_invalid_teacher_assignment():
    """Test assigning a teacher with a nonexistent teacher_id."""
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 99})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid teacher_id provided"  # Ensuring the error message is as specified