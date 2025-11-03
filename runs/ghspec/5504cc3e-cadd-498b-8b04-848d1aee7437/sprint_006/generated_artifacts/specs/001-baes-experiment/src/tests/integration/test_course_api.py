```python
import pytest
from flask import json
from app import create_app, db
from src.models.course import Course  # Importing Course model
from src.models.teacher import Teacher  # Importing Teacher model
from src.services.course_service import get_course_with_teacher  # Importing service function

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')  # Create app in testing mode
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Setup the database schema
            # Create a sample teacher and course for testing
            teacher = Teacher(name="John Doe")
            db.session.add(teacher)
            db.session.commit()
            course = Course(title="Math 101", teacher_id=teacher.id)
            db.session.add(course)
            db.session.commit()
        yield client  # This will provide the test client to the tests

def test_get_course_with_teacher_success(client):
    """Test getting a course with its associated teacher successfully."""
    # Request the course along with the teacher information
    response = client.get('/api/v1/courses/1')  # Assuming course ID is 1
    assert response.status_code == 200  # Check response status
    data = json.loads(response.data)
    
    # Validate the structure of the response
    assert 'id' in data
    assert 'title' in data
    assert 'teacher' in data
    assert data['teacher']['name'] == "John Doe"  # Verify teacher's name

def test_get_course_with_teacher_not_found(client):
    """Test getting a course that doesn't exist."""
    response = client.get('/api/v1/courses/999')  # Non-existing course ID
    assert response.status_code == 404  # Check for not found response
    data = json.loads(response.data)
    
    # Validate the error response structure
    assert 'error' in data
    assert data['error']['code'] == 'E404'  # Assuming code for not found
    assert data['error']['message'] == 'Course not found'  # Check message

def test_get_course_with_teacher_invalid_id(client):
    """Test getting a course with an invalid ID."""
    response = client.get('/api/v1/courses/not_an_integer')  # Invalid ID
    assert response.status_code == 400  # Check for bad request response
    data = json.loads(response.data)
    
    # Validate the error response structure
    assert 'error' in data
    assert data['error']['code'] == 'E400'  # Assuming code for invalid ID
    assert data['error']['message'] == 'Invalid course ID format'  # Check message
```