```python
import json
import pytest
from app import app, db
from models import Teacher, Course  # Importing the Teacher and Course models for testing

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables
        yield client
        db.drop_all()  # Cleanup after each test

def test_create_teacher_success(client):
    """Test that creating a teacher with valid data succeeds."""
    response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert 'id' in response.get_json()

def test_assign_teacher_to_course_success(client):
    """Test successful assignment of a Teacher to a Course."""
    # First create a Teacher for the test
    teacher_response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert teacher_response.status_code == 200
    teacher_id = teacher_response.get_json()['id']

    # Create a Course for assignment
    course_response = client.post('/courses', json={"title": "Mathematics", "description": "Intro Math"})
    assert course_response.status_code == 200
    course_id = course_response.get_json()['id']

    # Assign the created Teacher to the Course
    assignment_response = client.post(f'/courses/{course_id}/assign_teacher', json={"teacher_id": teacher_id})
    assert assignment_response.status_code == 200
    assert assignment_response.get_json()['message'] == "Teacher assigned successfully"

    # Retrieve the course to verify the assignment
    retrieve_response = client.get(f'/courses/{course_id}')
    assert retrieve_response.status_code == 200
    course_data = retrieve_response.get_json()
    assert course_data['teacher_id'] == teacher_id  # Verify teacher_id is linked to the course

def test_assign_teacher_invalid_id(client):
    """Test that assignment of a Teacher with an invalid ID fails gracefully."""
    # Create a Course for assignment
    course_response = client.post('/courses', json={"title": "Mathematics", "description": "Intro Math"})
    assert course_response.status_code == 200
    course_id = course_response.get_json()['id']

    # Attempt to assign a Teacher using an invalid Teacher ID
    invalid_teacher_id = 9999  # Assuming this ID doesn't exist
    assignment_response = client.post(f'/courses/{course_id}/assign_teacher', json={"teacher_id": invalid_teacher_id})
    assert assignment_response.status_code == 404  # Not found error for invalid ID
    assert "teacher not found" in assignment_response.get_json()["message"].lower()  # Check the message
```