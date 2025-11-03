import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.mark.parametrize("student_id, course_ids, expected_status, expected_response", [
    (1, [1], 200, {"id": 1, "course_ids": [1]}),
    (2, [1, 2], 200, {"id": 2, "course_ids": [1, 2]}),
    (3, [], 200, {"id": 3, "course_ids": []}),
    (1, None, 400, {"error": {"code": "E004", "message": "Course IDs must be provided"}}),
])
def test_associate_courses_to_student(student_id, course_ids, expected_status, expected_response):
    """Test associating Course IDs with a Student."""
    response = client.patch(f"/students/{student_id}/courses", json={"course_ids": course_ids})
    assert response.status_code == expected_status
    assert response.json() == expected_response

@pytest.mark.parametrize("student_id, expected_status, expected_response", [
    (1, 200, {"id": 1, "course_ids": [1]}),
    (2, 200, {"id": 2, "course_ids": [1, 2]}),
    (3, 200, {"id": 3, "course_ids": []}),
    (99, 404, {"error": {"code": "E005", "message": "Student not found"}}),
])
def test_get_student_with_courses(student_id, expected_status, expected_response):
    """Test retrieving a Student's details along with associated Course IDs."""
    response = client.get(f"/students/{student_id}")
    assert response.status_code == expected_status
    assert response.json() == expected_response