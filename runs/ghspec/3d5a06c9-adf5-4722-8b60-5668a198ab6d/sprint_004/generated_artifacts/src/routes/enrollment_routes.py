```python
import pytest

# Assuming the existence of a client fixture for the FastAPI application
@pytest.fixture
def client():
    from main import app  # Importing the FastAPI application
    from fastapi.testclient import TestClient
    return TestClient(app)

def test_enroll_student_in_course(client):
    # Step 1: Enroll a student in a course
    response = client.post('/enrollments', json={"student_id": 1, "course_id": 1})
    
    # Step 2: Validate the response
    assert response.status_code == 201  # Expecting 201 Created
    assert response.json() == {"message": "Enrollment successful"}

def test_retrieve_enrolled_courses(client):
    # Step 1: Get enrolled courses for the student
    response = client.get('/enrollments/1')  # Assuming student ID 1
    
    # Step 2: Validate the response
    assert response.status_code == 200  # Expecting 200 OK
    assert isinstance(response.json(), list)  # Expecting a list of courses
    
    # Optional: Check that at least one course is returned
    assert len(response.json()) > 0

def test_enroll_student_missing_ids(client):
    # Step 1: Attempt to enroll a student with missing IDs
    response = client.post('/enrollments', json={"student_id": None, "course_id": 1})
    
    # Step 2: Validate the response
    assert response.status_code == 400  # Expecting 400 Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "Student ID is required"}}

    response = client.post('/enrollments', json={"student_id": 1, "course_id": None})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Course ID is required"}}
```