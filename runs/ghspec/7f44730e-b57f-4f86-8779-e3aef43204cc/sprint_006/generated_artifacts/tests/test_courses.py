# tests/test_courses.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

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
    course_data = response.json()
    assert "teacher" in course_data["course"]
    assert course_data["course"]["teacher"]["name"] == "John Doe"  # Replace with the actual teacher's name expected
    assert course_data["course"]["teacher"]["email"] == "john.doe@example.com"  # Replace with the actual teacher's email expected

def test_assign_teacher_to_non_existent_teacher():
    """Test assigning a non-existent teacher to an existing course."""
    response = client.post("/courses/course1/assign_teacher", json={"teacher_id": "invalid_teacher_id"})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Teacher does not exist"}}