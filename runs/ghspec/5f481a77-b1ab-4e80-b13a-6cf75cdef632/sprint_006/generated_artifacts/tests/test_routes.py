```python
import pytest
from flask import json
from src.app import app  # Assuming the Flask app is initialized in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Existing test function example for creating a course
def test_create_course_with_valid_data(client):
    """Test the creation of a course with valid data."""
    response = client.post('/courses', data=json.dumps({
        'name': 'Introduction to Programming',
        'level': 'Beginner',
    }), content_type='application/json')
    assert response.status_code == 201  # Verify created status
    assert response.get_json()['name'] == 'Introduction to Programming'  # Verify course creation

def test_assign_teacher_to_course(client):
    """Test assigning a teacher to a course."""
    # First, create a course to assign a teacher to
    course_response = client.post('/courses', data=json.dumps({
        'name': 'Advanced Mathematics',
        'level': 'Advanced',
    }), content_type='application/json')
    assert course_response.status_code == 201
    course_id = course_response.get_json()['id']  # Get the created course ID

    # Assign a teacher to the created course
    response = client.post(f'/courses/{course_id}/assign-teacher', data=json.dumps({
        'teacher_id': 1
    }), content_type='application/json')
    
    assert response.status_code == 200  # Verify success status
    assert response.get_json()['teacher']['id'] == 1  # Verify teacher association
    assert response.get_json()['course']['id'] == course_id  # Verify course association

def test_retrieve_courses_with_teacher_details(client):
    """Test retrieving courses with teacher assigned details."""
    # Create a course and assign a teacher (assuming id 1 exists)
    course_response = client.post('/courses', data=json.dumps({
        'name': 'Data Science',
        'level': 'Intermediate',
    }), content_type='application/json')
    assert course_response.status_code == 201
    course_id = course_response.get_json()['id']  # Get the created course ID

    # Assign a teacher to the created course
    client.post(f'/courses/{course_id}/assign-teacher', data=json.dumps({
        'teacher_id': 1
    }), content_type='application/json')
    
    # Retrieve courses with teacher details
    response = client.get('/courses')
    assert response.status_code == 200  # Verify retrieval success
    courses = response.get_json()
    assert len(courses) > 0  # Ensure we have courses listed
    assert any(course['id'] == course_id and course['teacher']['id'] == 1 for course in courses)  # Check course-teacher association
```