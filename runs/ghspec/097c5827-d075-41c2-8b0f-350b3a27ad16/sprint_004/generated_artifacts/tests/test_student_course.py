```python
import pytest
from flask import json
from src.app import app
from src.models import Student, Course

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_link_student_to_courses(client):
    """Test case for linking a student to courses successfully."""
    response = client.post('/students/1/courses', data=json.dumps({
        'course_ids': [2, 3]
    }), content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == 1
    assert len(data['courses']) == 2
    assert all(course['id'] in [2, 3] for course in data['courses'])

def test_link_student_to_courses_invalid_ids(client):
    """Test case for linking a student to courses with invalid course IDs."""
    response = client.post('/students/1/courses', data=json.dumps({
        'course_ids': [999]  # Assuming 999 is an invalid ID
    }), content_type='application/json')

    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

def test_retrieve_student_courses(client):
    """Test case for retrieving courses linked to a student."""
    response = client.get('/students/1/courses')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == 1
    assert len(data['courses']) > 0  # Assuming there are courses linked

def test_add_course_to_student(client):
    """Test case for adding a new course to a student."""
    response = client.post('/students/1/courses', data=json.dumps({
        'course_ids': [4]  # Assuming 4 is a new valid course ID
    }), content_type='application/json')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert 4 in [course['id'] for course in data['courses']]

def test_remove_course_from_student(client):
    """Test case for removing a course from a student's record."""
    # Assuming we first link the student to a couple of courses
    client.post('/students/1/courses', data=json.dumps({
        'course_ids': [2, 3]
    }), content_type='application/json')

    response = client.post('/students/1/courses', data=json.dumps({
        'course_ids': [2]  # Now attempt to remove course 3 (not including it)
    }), content_type='application/json')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert 3 not in [course['id'] for course in data['courses']]
    assert 2 in [course['id'] for course in data['courses']]
```