```python
import pytest
from flask import json
from src.app import app
from src.models import Student, Course

@pytest.fixture
def client():
    """Create a test client for the application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_link_student_to_courses(client):
    """Test case for linking a student to courses."""
    response = client.post('/students/1/courses', data=json.dumps({
        'course_ids': [2, 3]
    }), content_type='application/json')
    
    # Check if the response status code is 200 OK
    assert response.status_code == 200
    data = response.get_json()
    
    # Validate the response contains expected student details
    assert data['id'] == 1
    assert 'courses' in data
    assert len(data['courses']) == 2  # Check if 2 courses were linked

def test_retrieve_student_courses(client):
    """Test case for retrieving courses linked to a student."""
    response = client.get('/students/1/courses')
    
    # Ensure successful retrieval
    assert response.status_code == 200
    data = response.get_json()
    
    # Validate the response contains course details
    assert isinstance(data['courses'], list)  # Check if courses is a list
    assert len(data['courses']) > 0  # Check if there are courses linked

def test_add_course_to_existing_student(client):
    """Test case for adding a new course to a student who already has courses."""
    response = client.post('/students/1/courses', data=json.dumps({
        'course_ids': [4]
    }), content_type='application/json')
    
    assert response.status_code == 200
    data = response.get_json()
    
    # Check the updated course count for the student
    assert len(data['courses']) > 2  # Verify the student now has more courses

def test_remove_course_from_student(client):
    """Test case for removing a course from a student's linked courses."""
    response = client.delete('/students/1/courses/3')  # Assuming 3 is the course ID to remove
    
    # Ensure successful removal
    assert response.status_code == 200
    data = response.get_json()
    
    # Validate that the course has been removed
    assert 3 not in [course['id'] for course in data['courses']]

def test_link_invalid_course(client):
    """Test case for linking a student to invalid course IDs."""
    response = client.post('/students/1/courses', data=json.dumps({
        'course_ids': [999]  # Assuming 999 does not exist
    }), content_type='application/json')

    # Expect an error for invalid course ID
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Assuming we define this error code for invalid input
    assert 'Invalid course IDs' in data['error']['message']

def test_link_to_non_existent_student(client):
    """Test case for linking courses to a non-existent student."""
    response = client.post('/students/999/courses', data=json.dumps({
        'course_ids': [2, 3]
    }), content_type='application/json')

    # Expect a 404 error for a nonexistent student
    assert response.status_code == 404
    data = response.get_json()
    assert data['error']['code'] == 'E002'  # Assuming we define this error code for non-existent resources
    assert 'Student not found' in data['error']['message']
```