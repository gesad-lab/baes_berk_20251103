```python
import pytest
from flask import json
from your_app import create_app, db  # make sure to replace with actual import paths
from your_app.models import Course, Enrollment  # update with actual model imports

@pytest.fixture
def client():
    app = create_app('testing')  # use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # create the database schema
            # Setup initial data for tests
            course = Course(name="Introduction to Programming", level="Beginner")
            db.session.add(course)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_enroll_student_in_course_success(client):
    """Test enrolling a student in a course successfully."""
    # Arrange
    student_id = 1
    course_id = 1
    enrollment_data = {
        "student_id": student_id,
        "course_id": course_id
    }
    
    # Act
    response = client.post('/enrollments', data=json.dumps(enrollment_data), content_type='application/json')
    
    # Assert
    assert response.status_code == 201  # Check for successful enrollment
    json_data = response.get_json()
    assert json_data['message'] == 'Enrollment successful'
    assert json_data['data']['student_id'] == student_id
    assert json_data['data']['course_id'] == course_id

def test_get_courses_for_student_success(client):
    """Test retrieving a list of courses for a specific student."""
    # Arrange
    student_id = 1
    course_id = 1
    enrollment_data = {
        "student_id": student_id,
        "course_id": course_id
    }
    client.post('/enrollments', data=json.dumps(enrollment_data), content_type='application/json')
    
    # Act
    response = client.get(f'/students/{student_id}/courses')
    
    # Assert
    assert response.status_code == 200  # Check for successful retrieval
    json_data = response.get_json()
    assert isinstance(json_data['courses'], list)  # Ensure courses is a list
    assert len(json_data['courses']) > 0  # Ensure there's at least one course

def test_enroll_student_in_nonexistent_course(client):
    """Test error handling for enrolling in a non-existent course."""
    # Arrange
    student_id = 1
    non_existent_course_id = 999
    enrollment_data = {
        "student_id": student_id,
        "course_id": non_existent_course_id
    }
    
    # Act
    response = client.post('/enrollments', data=json.dumps(enrollment_data), content_type='application/json')
    
    # Assert
    assert response.status_code == 404  # Check for failure response
    json_data = response.get_json()
    assert json_data['error']['message'] == 'Course not found'
    assert json_data['error']['code'] == 'E001'  # Assuming E001 is the code for invalid course

# Add additional tests for other scenarios if needed
```