```python
import json
import pytest
from api import create_app, db
from api.models import Course, Student  # Assuming the Student model is defined in models.py


@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        # Set up sample data for testing
        course1 = Course(name='Mathematics')
        course2 = Course(name='Science')
        student = Student(name='John Doe')
        db.session.add(course1)
        db.session.add(course2)
        db.session.add(student)
        db.session.commit()  # Commit the sample data
        yield app.test_client()  # Create the test client
        db.drop_all()  # Clean up

def test_assign_courses_to_student(test_client):
    """Test the assignment of courses to a student."""
    response = test_client.post('/students/1/courses', json={'course_ids': [1, 2]})
    
    assert response.status_code == 200  # Check for successful response
    data = json.loads(response.data)
    assert 'courses' in data
    assert len(data['courses']) == 2  # Verify both courses were assigned

def test_assign_invalid_courses_to_student(test_client):
    """Test assigning invalid course IDs to a student."""
    response = test_client.post('/students/1/courses', json={'course_ids': [999]})
    
    assert response.status_code == 400  # Check for bad request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Validate error code for invalid courses
    assert 'The specified courses do not exist.' in data['error']['message']

def test_update_student_courses(test_client):
    """Test adding/removing courses for a student."""
    # First, assign valid courses
    response = test_client.post('/students/1/courses', json={'course_ids': [1]})
    assert response.status_code == 200
    
    # Now, try to remove the course (assuming an endpoint exists for that action)
    response = test_client.post('/students/1/courses', json={'course_ids': []})  # Assuming empty array removes courses
    assert response.status_code == 200  # Check for successful removal
    data = json.loads(response.data)
    assert len(data['courses']) == 0  # Verify courses are empty after removal

def test_view_student_with_courses(test_client):
    """Test retrieval of student data including enrolled courses."""
    response = test_client.get('/students/1')
    
    assert response.status_code == 200  # Check for successful retrieval
    data = json.loads(response.data)
    assert 'name' in data and data['name'] == 'John Doe'  # Verify student name
    assert 'courses' in data  # Ensure courses are included in response
```