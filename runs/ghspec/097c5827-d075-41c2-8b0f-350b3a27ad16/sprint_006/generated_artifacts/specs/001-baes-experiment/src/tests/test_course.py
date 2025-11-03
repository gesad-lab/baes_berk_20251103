```python
# tests/test_course.py

import pytest
from flask import json
from src.app import app
from src.models import Course, Teacher
from src.database import db

@pytest.fixture
def client():
    """Create a test client for the application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_assign_teacher_to_course_success(client):
    """Test assigning a teacher to a course with valid inputs."""
    # Arrange: Create a teacher and a course record for testing
    teacher = Teacher(name='Jane Smith', email='jane.smith@example.com')
    course = Course(name='Mathematics 101', level='Beginner')
    
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()
    
    # Act: Send a PATCH request to assign the teacher to the course
    response = client.patch(f'/courses/{course.id}/assign-teacher', 
                             data=json.dumps({'teacherId': teacher.id}),
                             content_type='application/json')
                             
    # Assert: Check the response and the course record
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data == {'message': 'Teacher assigned successfully.'}
    
    # Verify that the course now has the teacherId assigned
    updated_course = Course.query.get(course.id)
    assert updated_course.teacherId == teacher.id

def test_assign_teacher_to_course_failure_invalid_teacher(client):
    """Test assigning a non-existent teacher to a course."""
    # Arrange: Create a course record for testing
    course = Course(name='Mathematics 101', level='Beginner')
    db.session.add(course)
    db.session.commit()
    
    # Act: Send a PATCH request to assign a non-existent teacher
    response = client.patch(f'/courses/{course.id}/assign-teacher', 
                             data=json.dumps({'teacherId': 999}),  # Invalid ID
                             content_type='application/json')
                             
    # Assert: Check the response for appropriate error message
    assert response.status_code == 400
    response_data = json.loads(response.data)
    assert response_data == {'error': {'code': 'E001', 'message': 'Invalid teacher ID.'}}

def test_get_course_details_with_teacher(client):
    """Test retrieving course details, including teacher information."""
    # Arrange: Create a teacher and a course record
    teacher = Teacher(name='Jane Smith', email='jane.smith@example.com')
    course = Course(name='Mathematics 101', level='Beginner', teacherId=teacher.id)
    
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()
    
    # Act: Send a GET request to retrieve course details
    response = client.get(f'/courses/{course.id}')
    
    # Assert: Check the response
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['courseId'] == course.id
    assert response_data['courseName'] == course.name
    assert response_data['level'] == course.level
    assert response_data['teacher']['id'] == teacher.id
    assert response_data['teacher']['name'] == teacher.name
    assert response_data['teacher']['email'] == teacher.email

def test_get_course_details_not_found(client):
    """Test retrieving course details for a non-existent course."""
    # Act: Send a GET request to retrieve details of a non-existent course
    response = client.get('/courses/999')  # Invalid ID

    # Assert: Check the response for appropriate error message
    assert response.status_code == 404
    response_data = json.loads(response.data)
    assert response_data == {'error': {'code': 'E002', 'message': 'Course not found.'}}
```