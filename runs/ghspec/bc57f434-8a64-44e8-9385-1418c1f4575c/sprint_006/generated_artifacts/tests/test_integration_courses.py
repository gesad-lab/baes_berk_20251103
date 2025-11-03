```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is in src/main.py
from src.models import CourseResponse, TeacherResponse  # Importing necessary models

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_fetch_course_with_teacher(test_client):
    """Integration test for fetching course details along with assigned teacher."""
    
    # Assuming a course with ID 1 exists and has a teacher assigned
    course_id = 1  
    response = test_client.get(f"/courses/{course_id}")
    
    assert response.status_code == 200
    course_data = response.json()
    
    # Check that the response structure is as expected
    assert "id" in course_data
    assert "name" in course_data
    assert "teacher" in course_data  # Ensure teacher data is included
    
    # Check teacher details
    teacher = course_data["teacher"]
    assert "id" in teacher
    assert "name" in teacher
    assert "email" in teacher

def test_assign_teacher_to_course(test_client):
    """Integration test for assigning a teacher to a course."""
    
    # Assuming a teacher with ID 1 and a course with ID 1 exist
    teacher_id = 1
    course_id = 1
    response = test_client.post(f"/courses/{course_id}/assign-teacher", json={"teacher_id": teacher_id})
    
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully."}

    # Fetching the updated course to verify the assignment
    fetch_response = test_client.get(f"/courses/{course_id}")
    assert fetch_response.status_code == 200
    course_data = fetch_response.json()
    assert course_data["teacher"]["id"] == teacher_id
```