```python
import pytest
from flask import json
from src.routes import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_course_with_valid_data(client):
    """Test creating a new course with valid name and level."""
    response = client.post('/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    assert response.status_code == 201
    assert 'course' in response.json
    assert response.json['course']['name'] == 'Mathematics'

def test_create_teacher_with_valid_data(client):
    """Test creating a new teacher with valid name and email."""
    response = client.post('/teachers', json={'name': 'Jane Doe', 'email': 'jane.doe@example.com'})
    assert response.status_code == 201
    assert 'teacher' in response.json
    assert response.json['teacher']['name'] == 'Jane Doe'

def test_create_teacher_without_name(client):
    """Test creating a teacher without a name."""
    response = client.post('/teachers', json={'email': 'jane.doe@example.com'})
    assert response.status_code == 400
    assert response.json['error']['message'] == 'Name is required.'

def test_create_teacher_with_invalid_email(client):
    """Test creating a teacher with an incorrectly formatted email."""
    response = client.post('/teachers', json={'name': 'Jane Doe', 'email': 'invalid-email'})
    assert response.status_code == 400
    assert response.json['error']['message'] == 'Invalid email format.'
```