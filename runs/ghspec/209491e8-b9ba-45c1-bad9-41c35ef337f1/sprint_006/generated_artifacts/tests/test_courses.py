# tests/test_courses.py
import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

# Test assignment of teacher to course
def test_assign_teacher_to_course(client):
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully."}

# Test retrieval of course with teacher information
def test_get_course_with_teacher(client):
    response = client.get("/courses/1")  # assuming this ID exists
    assert response.status_code == 200
    json_response = response.json()
    assert "teacher" in json_response  # Check that teacher info is included
    assert "name" in json_response["teacher"]  # Ensure name field is present
    assert json_response["teacher"]["id"] == 1  # Ensure correct teacher ID is returned

# Test validation handling for assigning teacher to non-existing course
def test_assign_teacher_invalid_course(client):
    response = client.post("/courses/999/assign-teacher", json={"teacher_id": 1})  # Invalid course ID
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E001"  # Check specific error code

# Test validation handling for assigning teacher with invalid teacher ID
def test_assign_teacher_invalid_teacher(client):
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 999})  # Invalid teacher ID
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E002"  # Check specific error code for invalid teacher

# Test retrieval of course that does not exist
def test_get_course_invalid_id(client):
    response = client.get("/courses/999")  # Invalid course ID
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E001"  # Check error code for not found