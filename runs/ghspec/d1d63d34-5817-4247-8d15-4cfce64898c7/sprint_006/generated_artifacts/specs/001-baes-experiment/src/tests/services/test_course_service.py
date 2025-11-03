```python
import pytest
from fastapi.testclient import TestClient
from src.services.course_service import app

client = TestClient(app)

@pytest.fixture
def valid_teacher():
    return {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }

@pytest.fixture
def create_teacher(valid_teacher):
    """Fixture to create a teacher for testing purposes."""
    response = client.post("/teachers", json=valid_teacher)
    assert response.status_code == 201
    return response.json()

@pytest.fixture
def valid_course():
    return {
        "name": "Mathematics",
        "description": "An introductory course on Mathematics."
    }

@pytest.fixture
def create_course(valid_course):
    """Fixture to create a course for testing purposes."""
    response = client.post("/courses", json=valid_course)
    assert response.status_code == 201
    return response.json()

def test_remove_teacher_from_course(create_teacher, create_course):
    # First assign the teacher to the course
    assign_response = client.post(
        f"/courses/{create_course['id']}/assign-teacher",
        json={"teacher_id": create_teacher["id"]}
    )
    assert assign_response.status_code == 201
    
    # Now remove the teacher from the course
    response = client.delete(f"/courses/{create_course['id']}/remove-teacher")
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher has been removed from the Course."}

def test_remove_teacher_from_nonexistent_course(create_teacher):
    response = client.delete("/courses/999/remove-teacher")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found."}}

def test_remove_teacher_when_no_teacher_assigned(create_course):
    # Try to remove a teacher from a course that has no teacher assigned
    response = client.delete(f"/courses/{create_course['id']}/remove-teacher")
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E400", "message": "No teacher is currently assigned to this Course."}}
```