```python
import json
import pytest
from api import create_app, db
from api.models import Course, Teacher  # Assuming Teacher and Course models are defined

@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()

def test_assign_teacher_to_non_existing_course(test_client):
    """Test assigning a teacher to a non-existent course."""
    response = test_client.post('/courses/999/assign-teacher', json={'teacher_id': 1})
    assert response.status_code == 404
    assert json.loads(response.data) == {"error": {"code": "E404", "message": "Course not found."}}

def test_assign_teacher_with_invalid_teacher_id(test_client):
    """Test assigning a teacher with an invalid teacher ID."""
    # Create a valid course first
    course_data = {"name": "Mathematics", "description": "Mathematics Course"}
    test_client.post('/courses', json=course_data)

    response = test_client.post('/courses/1/assign-teacher', json={'teacher_id': 999})
    assert response.status_code == 400
    assert json.loads(response.data) == {"error": {"code": "E400", "message": "Invalid teacher ID."}}

def test_update_teacher_assignment_to_course(test_client):
    """Test updating the teacher assignment for a course."""
    # Create a valid teacher and course first
    teacher_data = {"name": "John Doe", "email": "john.doe@example.com"}
    test_client.post('/teachers', json=teacher_data)
    
    course_data = {"name": "Science", "description": "Science Course"}
    test_client.post('/courses', json=course_data)

    # Assign teacher to course
    response = test_client.post('/courses/1/assign-teacher', json={'teacher_id': 1})
    assert response.status_code == 200

    # Update teacher to a different valid teacher
    new_teacher_data = {"name": "Jane Smith", "email": "jane.smith@example.com"}
    test_client.post('/teachers', json=new_teacher_data)

    response = test_client.post('/courses/1/assign-teacher', json={'teacher_id': 2})
    assert response.status_code == 200
    updated_course = json.loads(response.data)
    assert updated_course['teacher_id'] == 2

def test_get_course_with_teacher_details(test_client):
    """Test retrieving course information including teacher details."""
    # Create a valid teacher and course first
    teacher_data = {"name": "Alice Cooper", "email": "alice.cooper@example.com"}
    test_client.post('/teachers', json=teacher_data)
    
    course_data = {"name": "History", "description": "History Course"}
    test_client.post('/courses', json=course_data)

    # Assign teacher to course
    test_client.post('/courses/1/assign-teacher', json={'teacher_id': 1})

    response = test_client.get('/courses/1')
    assert response.status_code == 200
    result = json.loads(response.data)
    assert 'teacher' in result
    assert result['teacher']['name'] == "Alice Cooper"
    assert result['teacher']['email'] == "alice.cooper@example.com"
```