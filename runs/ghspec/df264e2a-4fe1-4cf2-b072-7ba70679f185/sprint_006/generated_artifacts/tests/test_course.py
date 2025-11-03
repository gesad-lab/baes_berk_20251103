```python
import pytest

def test_assign_teacher_to_course(client):
    """Test successful assignment of a teacher to a course."""
    response = client.patch("/courses/1/assign-teacher", json={"teacher_id": "1"})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned to course successfully."}

def test_assign_teacher_to_non_existing_course(client):
    """Test error handling when assigning a teacher to a non-existing course."""
    response = client.patch("/courses/999/assign-teacher", json={"teacher_id": "1"})
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Course not found."
        }
    }

def test_retrieve_course_with_teacher(client):
    """Test retrieving a course's details that include teacher information."""
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()

def test_retrieve_non_existing_course(client):
    """Test retrieving a course that does not exist."""
    response = client.get("/courses/999")
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E003",
            "message": "Course not found."
        }
    }
```