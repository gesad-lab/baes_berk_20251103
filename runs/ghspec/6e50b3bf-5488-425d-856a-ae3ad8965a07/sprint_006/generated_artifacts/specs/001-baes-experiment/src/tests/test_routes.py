```python
import pytest
from flask import json
from src.routes import app, db
from src.models import Teacher, Course  # Importing the new Course model
from src.services import create_teacher, create_course  # Importing service functions for creating entities

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DATABASE'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables for the test
            yield client  # Yield the test client for use in tests
            db.drop_all()  # Drop all tables after tests

def test_create_teacher(client):
    """Test endpoint for creating a new teacher."""
    response = client.post('/teachers', 
                            data=json.dumps({"name": "Jane Doe", "email": "jane.doe@example.com"}),
                            content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data  # Ensure teacher ID is returned
    assert data['name'] == "Jane Doe"

def test_create_course(client):
    """Test endpoint for creating a new course."""
    # First, create a teacher to link to the course
    teacher_response = client.post('/teachers', 
                                    data=json.dumps({"name": "John Teacher", "email": "john.teacher@example.com"}),
                                    content_type='application/json')
    teacher_id = json.loads(teacher_response.data)['id']

    # Now, create a course and link it to the teacher
    response = client.post('/courses', 
                            data=json.dumps({"title": "Math 101", "teacher_id": teacher_id}),
                            content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data  # Ensure course ID is returned
    assert data['title'] == "Math 101"
    assert data['teacher_id'] == teacher_id  # Verify course is assigned to the correct teacher

def test_create_course_invalid_teacher(client):
    """Test creating a course with an invalid teacher ID."""
    response = client.post('/courses', 
                            data=json.dumps({"title": "Science 101", "teacher_id": 999}),  # Non-existing teacher ID
                            content_type='application/json')
    assert response.status_code == 400  # Bad request expected
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'  # Error code for invalid teacher ID
    assert 'message' in data['error']  # Ensure an error message is provided
```