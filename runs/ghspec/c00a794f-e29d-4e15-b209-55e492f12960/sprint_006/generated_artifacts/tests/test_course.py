# tests/test_course.py
import pytest
from fastapi import status
from src.models import Course, Teacher
from src.database import SessionLocal

@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from src.main import app
    return TestClient(app)

def test_assign_teacher_to_course(client):
    # Assuming a course with ID 1 exists and a teacher with ID 1 exists
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully."}

def test_assign_teacher_without_teacher(client):
    # Attempt to assign a teacher without specifying a teacher_id
    response = client.post("/courses/1/assign_teacher", json={})
    assert response.status_code == 400  # Expecting a bad request status code
    assert response.json() == {"error": {"code": "E001", "message": "A teacher must be selected."}}

def test_retrieve_course_information_with_teacher_details(client):
    # Assuming course with ID 1 has teacher assigned with ID 1
    response = client.get("/courses/1")
    assert response.status_code == 200
    course_data = response.json()
    assert "teacher" in course_data  # Check if the teacher data is included
    assert course_data["teacher"]["id"] == 1  # Ensure the correct teacher is returned
    assert "name" in course_data["teacher"]  # Check for teacher's name field
    assert "email" in course_data["teacher"]  # Check for teacher's email

def test_database_migration_validation(client):
    # Test to verify that the relationships are properly established post-migration
    response = client.get("/courses")
    assert response.status_code == 200
    courses = response.json()
    for course in courses:
        assert "teacher" in course  # Each course should reference a teacher
        if course["teacher"]:
            assert "id" in course["teacher"]  # Teacher should have an ID
            assert "name" in course["teacher"]  # Teacher should have a name
            assert "email" in course["teacher"]  # Teacher should have an email
