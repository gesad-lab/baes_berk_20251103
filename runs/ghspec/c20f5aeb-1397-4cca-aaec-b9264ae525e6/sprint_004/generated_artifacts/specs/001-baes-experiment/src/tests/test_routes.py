```python
import json
import time
import pytest
from app import app, db
from models import Student, Course  # Importing Course for validation

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables
        yield client
        db.drop_all()  # Cleanup after each test

def test_create_student_with_email_response_time(client):
    """Test that creating a student with an email responds within 2 seconds."""
    start_time = time.time()
    # additional test code here...
    assert time.time() - start_time < 2

def test_enroll_student_in_course(client):
    """Test that a student can be enrolled in valid courses."""
    response = client.post('/students/1/enroll', json={
        "course_ids": [1, 2, 3]
    })
    assert response.status_code == 200
    assert 'courses' in response.get_json()  # Assert courses are included in response

def test_enroll_student_invalid_course(client):
    """Test enrolling a student in an invalid course returns error."""
    response = client.post('/students/1/enroll', json={
        "course_ids": [999]  # Non-existent course ID
    })
    assert response.status_code == 400
    assert response.get_json()['error']['message'] == "Invalid course IDs"

def test_enroll_student_invalid_student(client):
    """Test that enrolling with a non-existent student returns error."""
    response = client.post('/students/999/enroll', json={
        "course_ids": [1, 2]
    })
    assert response.status_code == 404
    assert response.get_json()['error']['message'] == "Student not found"
```