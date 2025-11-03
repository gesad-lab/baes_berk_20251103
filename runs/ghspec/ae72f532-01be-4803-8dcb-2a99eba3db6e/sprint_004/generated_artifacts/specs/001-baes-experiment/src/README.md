```plaintext
# File: tests/test_student_routes.py
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.mark.parametrize("student_id, expected_courses, expected_status", [
    (1, {"course_ids": [1, 2]}, 200),
    (2, {"course_ids": [1]}, 200),
])
def test_retrieve_student_courses(student_id, expected_courses, expected_status):
    """Test retrieving a student's enrolled courses"""
    response = client.get(f"/students/{student_id}/courses")
    assert response.status_code == expected_status
    assert response.json() == expected_courses

@pytest.mark.parametrize("student_id, course_ids, expected_status, expected_response", [
    (1, [1, 2], 200, {"student_id": 1, "course_ids": [1, 2]}),
    (1, [99], 400, {"error": {"code": "E002", "message": "Invalid course IDs", "details": {"invalid_ids": [99]}}}),
])
def test_enroll_student_in_courses(student_id, course_ids, expected_status, expected_response):
    """Test enrolling a student in courses"""
    response = client.post(f"/students/{student_id}/enroll", json={"course_ids": course_ids})
    assert response.status_code == expected_status
    assert response.json() == expected_response

def test_data_integrity_after_enrollment():
    """Test that existing student records remain intact after course enrollment"""
    response = client.get("/students/1")
    assert response.status_code == 200
    # Ensure existing data is still present and correct
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "course_ids": [1, 2],  # Assuming these courses exist
    }
```