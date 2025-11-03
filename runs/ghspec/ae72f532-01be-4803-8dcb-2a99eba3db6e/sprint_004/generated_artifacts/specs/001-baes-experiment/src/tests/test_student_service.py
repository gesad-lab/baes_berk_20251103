```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.mark.parametrize("student_id, course_ids, expected_status, expected_response", [
    (1, [1, 2], 200, {"id": 1, "course_ids": [1, 2]}),
    (2, [], 200, {"id": 2, "course_ids": []}),
    (3, [999], 400, {"error": {"code": "E004", "message": "Invalid Course IDs: [999]"}}),
])
def test_associate_courses_with_student(student_id, course_ids, expected_status, expected_response):
    """Test associating courses with a student by ID and checking response."""
    response = client.put(f"/students/{student_id}/courses", json={"course_ids": course_ids})
    assert response.status_code == expected_status
    assert response.json() == expected_response

@pytest.mark.parametrize("student_id, expected_status, expected_response", [
    (1, 200, {"id": 1, "course_ids": [1, 2]}),
    (2, 200, {"id": 2, "course_ids": []}),
    (999, 404, {"error": {"code": "E005", "message": "Student not found"}}),
])
def test_get_student_courses(student_id, expected_status, expected_response):
    """Test retrieving a student's enrolled courses."""
    response = client.get(f"/students/{student_id}/courses")
    assert response.status_code == expected_status
    assert response.json() == expected_response

def test_update_student_with_non_existent_courses():
    """Test handling of enrolling a student in non-existent courses."""
    response = client.put("/students/1/courses", json={"course_ids": [999]})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E004", "message": "Invalid Course IDs: [999]"}}
```