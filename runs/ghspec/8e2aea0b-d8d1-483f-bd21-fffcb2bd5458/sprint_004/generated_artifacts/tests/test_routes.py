```python
import json
import pytest
from flask import Flask
from flask.testing import FlaskClient
from src.app import create_app
from src.models import db, Course, Student  # Assuming the Student model is defined in models.py

@pytest.fixture
def client() -> FlaskClient:
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            # Create the database and add test data
            db.create_all()
            # Insert test data for students and courses
            test_student = Student(name="Test Student")
            test_course = Course(name="Test Course")
            db.session.add(test_student)
            db.session.add(test_course)
            db.session.commit()
            yield client
            db.session.remove()
            db.drop_all()

def test_view_student_courses(client):
    """Test retrieving all courses for a specific student."""
    # Assuming the endpoint is defined as /students/{student_id}/courses
    response = client.get('/students/1/courses')  # Assuming student ID is 1
    assert response.status_code == 200  # Check if the response is OK
    data = response.get_json()
    assert isinstance(data, list)  # Expect a list of courses
    assert len(data) == 0  # Initially, no courses should be associated

    # Enroll the student in a course
    enroll_response = client.post('/students/1/enroll', 
        json={"course_id": 1})  # Enroll in test course ID 1
    assert enroll_response.status_code == 200  # Ensure enrollment is successful

    # Now retrieve the courses again
    response = client.get('/students/1/courses')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1  # Now the student has one course
    assert data[0]['id'] == 1  # The ID of the enrolled course should match

def test_enroll_student_in_non_existing_course(client):
    """Test error handling when attempting to enroll a student in a non-existing course."""
    # Attempt to enroll in a non-existing course (ID 999)
    response = client.post('/students/1/enroll', 
        json={"course_id": 999})  # Non-existing course ID
    assert response.status_code == 400  # Expect a bad request due to invalid course ID
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Assuming the error code for invalid course is E001
    assert 'Invalid course ID' in data['error']['message']  # Check for appropriate error message
```