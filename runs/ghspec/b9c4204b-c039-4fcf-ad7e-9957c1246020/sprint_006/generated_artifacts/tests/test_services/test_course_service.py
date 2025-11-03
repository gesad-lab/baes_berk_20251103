```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Main FastAPI application
from src.models import Course  # Importing Course model for response validation

client = TestClient(app)

@pytest.mark.integration
def test_associate_non_existent_teacher():
    """Test attempting to associate a non-existent teacher with a course."""
    
    # Given a course ID that exists in the database
    course_id = 1  # Assuming this is an existing course
    
    # When we attempt to associate a teacher with a non-existent ID
    non_existent_teacher_id = 999  # Assuming this ID does not exist
    
    response = client.put(
        f"/courses/{course_id}/associate_teacher",
        json={"teacher_id": non_existent_teacher_id}
    )
    
    # Then the response should indicate that the teacher does not exist
    assert response.status_code == 400  # Bad Request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Teacher ID does not exist"
        }
    }

@pytest.mark.integration
def test_associate_teacher_with_existing_course():
    """Test successfully associating an existing teacher with a course."""
    
    # Given a course ID and an existing teacher ID
    course_id = 1  # Assuming this is an existing course
    existing_teacher_id = 1  # Assuming this ID represents an existing teacher
    
    response = client.put(
        f"/courses/{course_id}/associate_teacher",
        json={"teacher_id": existing_teacher_id}
    )
    
    # Then the response should indicate success and return the updated course details
    assert response.status_code == 200  # Successful update
    assert response.json() == {
        "status": "success",
        "course_id": course_id,
        "teacher_id": existing_teacher_id
    }
```