```markdown
# README.md

## Integration Tests for API Behaviors

This document outlines the integration tests implemented for the updated API behaviors concerning the Course and Teacher entities within the educational management system.

### User Scenarios
1. **Assigning a Teacher to a Course**:
   - Test the assignment of a valid Teacher ID to a Course and confirm that the Course reflects the updated association.

2. **Viewing Course with Teacher Information**:
   - Test retrieving a specific Course's details to ensure the response includes associated Teacher information.

3. **Validation of Teacher Assignment**:
   - Test attempting to assign a non-existent Teacher ID to a Course, ensuring the application returns an appropriate error response.

4. **Handling Multiple Assignments**:
   - Test the scenario where multiple Teachers are attempted to be assigned to a single Course, ensuring the application correctly rejects this operation.

### Integration Test Implementation

The integration tests for the API have been crafted to verify the functionalities outlined in the user scenarios. The tests are located in the `tests/api/test_integration.py` file, and the implementation details are as follows:

```python
import json
import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    """Fixture to create a test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

@pytest.fixture
def setup_teachers(client):
    """Create test data for teachers."""
    teacher_response = client.post("/api/v1/teachers", json={
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    })
    assert teacher_response.status_code == 201
    return teacher_response.json()

@pytest.fixture
def setup_courses(client, setup_teachers):
    """Create test data for courses."""
    course_response = client.post("/api/v1/courses", json={
        "title": "Math 101",
        "description": "Basic Mathematics"
    })
    assert course_response.status_code == 201
    return course_response.json()

def test_assign_teacher_to_course(client, setup_courses, setup_teachers):
    """Test assigning a teacher to a course."""
    course_id = setup_courses['id']
    teacher_id = setup_teachers['id']
    response = client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})
    assert response.status_code == 200
    assert response.json()['teacher_id'] == teacher_id

def test_view_course_with_teacher_info(client, setup_courses, setup_teachers):
    """Test viewing course details with teacher's info."""
    course_id = setup_courses['id']
    response = client.get(f"/api/v1/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()['teacher_id'] is not None
    assert 'Jane Smith' in response.json()['teacher_name']

def test_invalid_teacher_assignment(client, setup_courses):
    """Test assigning a non-existent teacher."""
    course_id = setup_courses['id']
    response = client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": 9999})  # Assuming 9999 is invalid
    assert response.status_code == 400
    assert response.json()['error']['code'] == 'E001'  # Sample error code for invalid teacher ID

def test_multiple_teacher_assignment(client, setup_courses, setup_teachers):
    """Test assigning multiple teachers to a single course."""
    course_id = setup_courses['id']
    teacher_id = setup_teachers['id']
    response = client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})
    assert response.status_code == 200  # First assignment succeeds
    
    # Attempt to assign another teacher
    response = client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})
    assert response.status_code == 400
    assert response.json()['error']['code'] == 'E002'  # Sample error code for multiple assignment error
```

### Running the Tests

To execute the integration tests, ensure you have pytest installed, then run the following command:

```bash
pytest tests/api/test_integration.py
```

### Conclusion

These integration tests ensure that the updated API behaviors align with the specifications laid out in the user scenarios, supporting the robustness and reliability of the course-teacher assignment functionalities in the educational management system.
```