```python
import pytest
from flask import json
from app import create_app, db
from app.models import Course, Student

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Create the database tables
            
            # Set up sample data for testing
            sample_student = Student(name='John Doe')
            sample_course = Course(name='Sample Course', level='Beginner')
            db.session.add(sample_student)
            db.session.add(sample_course)
            db.session.commit()
            
            yield testing_client  # This allows the tests to run

            db.drop_all()  # Cleanup after tests

def test_enroll_student_in_course(test_client):
    """Test if a student can be enrolled in a course successfully."""
    response = test_client.post('/students/1/courses', 
                                 data=json.dumps({'course_id': 1}),
                                 content_type='application/json')
    assert response.status_code == 201  # Check for successful enrollment
    response_data = json.loads(response.data)
    assert response_data['student_id'] == 1
    assert response_data['course_id'] == 1

def test_list_students_courses(test_client):
    """Test if the courses for a student can be fetched successfully."""
    # Enroll student in course first
    test_client.post('/students/1/courses', 
                     data=json.dumps({'course_id': 1}),
                     content_type='application/json')
    
    response = test_client.get('/students/1/courses')
    assert response.status_code == 200  # Check successful retrieval
    response_data = json.loads(response.data)
    assert isinstance(response_data, list)  # Response should be a list
    assert len(response_data) == 1  # There should be one course listed
    assert response_data[0]['name'] == 'Sample Course'  # Verify course name

def test_unenroll_student_from_course(test_client):
    """Test if a student can be unenrolled from a course successfully."""
    # First ensure the student is enrolled
    test_client.post('/students/1/courses', 
                     data=json.dumps({'course_id': 1}),
                     content_type='application/json')
    
    response = test_client.delete('/students/1/courses/1')
    assert response.status_code == 204  # Check for successful unenrollment

    # Verify student no longer enrolled
    response = test_client.get('/students/1/courses')
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert len(response_data) == 0  # No courses should be listed after unenrollment
```