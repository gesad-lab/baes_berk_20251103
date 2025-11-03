```python
import pytest
from flask import json
from src.app import create_app  # Assuming you have a Flask application factory
from src.models import StudentCourse  # Import the StudentCourse model for testing

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_associate_student_with_course(client):
    """Test that associating a student with a course works correctly."""
    # Step 1: Create a student and a course if those endpoints exist
    student_response = client.post('/students', json={'name': 'John Doe'})
    course_response = client.post('/courses', json={'name': 'Mathematics'})

    assert student_response.status_code == 201  # Assuming 201 is returned for successful creation
    assert course_response.status_code == 201

    student_id = student_response.json['id']  # Assuming the response contains the Id of created student
    course_id = course_response.json['id']    # Assuming the response contains the Id of created course

    # Step 2: Associate the student with the course
    association_response = client.post('/student_courses', json={
        'student_id': student_id,
        'course_id': course_id
    })

    assert association_response.status_code == 201  # Check if the association was successful

    # Step 3: Verify the association was created in the database
    associations = StudentCourse.query.filter_by(student_id=student_id, course_id=course_id).all()
    assert len(associations) == 1  # Ensure there is exactly one association

def test_associate_student_with_nonexistent_course(client):
    """Test that associating a student with a nonexistent course returns an error."""
    student_response = client.post('/students', json={'name': 'Jane Doe'})
    assert student_response.status_code == 201
    student_id = student_response.json['id']

    # Attempt to associate with a non-existent course ID
    association_response = client.post('/student_courses', json={
        'student_id': student_id,
        'course_id': 9999  # Assuming this ID does not exist
    })

    assert association_response.status_code == 404  # Check if the error for nonexistent course is returned
    assert 'Course not found' in association_response.json['error']['message']

def test_associate_nonexistent_student_with_course(client):
    """Test that associating a nonexistent student with a course returns an error."""
    course_response = client.post('/courses', json={'name': 'Science'})
    assert course_response.status_code == 201
    course_id = course_response.json['id']

    # Attempt to associate non-existent student ID
    association_response = client.post('/student_courses', json={
        'student_id': 9999,  # Assuming this ID does not exist
        'course_id': course_id
    })

    assert association_response.status_code == 404  # Check if the error for nonexistent student is returned
    assert 'Student not found' in association_response.json['error']['message']
```