```python
import json
import pytest
from flask import Flask
from flask.testing import FlaskClient
from src.app import create_app  # Assuming there is a function to create your Flask app
from src.models import db, Course, Student  # Importing the Course and Student models

@pytest.fixture
def client() -> FlaskClient:
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            # Create the database and add test data
            db.create_all()
            # Adding initial test data for a student and a course
            course = Course(name="Biology 101")
            student = Student(name="John Doe")
            db.session.add(course)
            db.session.add(student)
            db.session.commit()
            yield client
            db.session.remove()
            db.drop_all()

def test_enroll_student_in_course(client):
    # Arrange: Create a student and a course
    response = client.post('/students/1/enroll', json={"course_id": 1})
    
    # Assert: Check if the response indicates successful enrollment
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == "Student successfully enrolled in course."
    assert data['student_id'] == 1
    assert data['course_id'] == 1

def test_view_student_courses(client):
    # Arrange: Enroll student in a course first
    client.post('/students/1/enroll', json={"course_id": 1})

    # Act: Retrieve the courses for this student
    response = client.get('/students/1/courses')

    # Assert: Ensure that the correct data is returned
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1  # One course enrolled
    assert data[0]['course_id'] == 1
    assert data[0]['name'] == "Biology 101"

def test_error_handling_invalid_enrollment(client):
    # Act: Attempt to enroll the student in a non-existing course
    response = client.post('/students/1/enroll', json={"course_id": 999})  # Assume 999 is an invalid course ID

    # Assert: Ensure that an appropriate error message is returned
    assert response.status_code == 400  # Assuming the endpoint returns a 400 for invalid course
    data = json.loads(response.data)
    assert data['error']['code'] == "E001"  # Assuming this is the error code for invalid course
    assert data['error']['message'] == "Course does not exist."
```