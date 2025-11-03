import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Setup logic for creating necessary records in the database
    # For example, create students and courses that the tests will use
    pass

def test_enroll_student_in_course():
    # Assuming we have a student with ID 1 and a course with ID 1
    response = client.post("/enroll", json={"student_id": 1, "course_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully enrolled student in course"}

def test_unenroll_student_from_course():
    # Assuming we have a student with ID 1 and a course with ID 1
    response = client.delete("/unenroll", json={"student_id": 1, "course_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully unenrolled student from course"}

def test_get_student_details():
    # Assuming we have a student with ID 1
    response = client.get("/students/1")
    assert response.status_code == 200
    assert "courses" in response.json()  # Ensure the student's course list is included

def test_enroll_student_with_invalid_course():
    # Assuming student with ID 1 exists, but course with ID 999 does not
    response = client.post("/enroll", json={"student_id": 1, "course_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}

def test_get_nonexistent_student():
    # Test retrieving a student that does not exist
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found"}}