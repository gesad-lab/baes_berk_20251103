# tests/test_teachers.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_teacher_valid():
    """Test creating a teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Teacher created successfully",
        "teacher": {
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }

def test_assign_teacher_to_course():
    """Test assigning a teacher to a course."""
    response = client.post("/courses/course1/assign_teacher", json={"teacher_id": "teacher123"})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned to course successfully"}

def test_assign_teacher_to_non_existent_course():
    """Test assigning a teacher to a non-existent course."""
    response = client.post("/courses/invalid_course_id/assign_teacher", json={"teacher_id": "teacher123"})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Course does not exist"}}

def test_get_course_details_with_teacher():
    """Test retrieving course details including assigned teacher."""
    response = client.get("/courses/course1")
    assert response.status_code == 200
    assert "teacher" in response.json()["course"]

def test_assign_non_existent_teacher_to_course():
    """Test assigning a non-existent teacher to an existing course."""
    response = client.post("/courses/course1/assign_teacher", json={"teacher_id": "invalid_teacher_id"})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Teacher does not exist"}}

def test_retrieve_course_details_with_assigned_teacher():
    """Test retrieving course details with the assigned teacher's information."""
    response = client.get("/courses/course1")
    assert response.status_code == 200
    course_data = response.json()
    assert "teacher" in course_data
    assert course_data["teacher"]["name"] == "John Doe"
    assert course_data["teacher"]["email"] == "john.doe@example.com"