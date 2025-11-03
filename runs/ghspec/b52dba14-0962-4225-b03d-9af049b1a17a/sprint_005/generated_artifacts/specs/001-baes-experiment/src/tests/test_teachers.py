```python
import pytest
from flask import json
from src.api.teacher_routes import create_teacher, get_teacher
from src.models.teacher_model import Teacher
from src.services.teacher_service import TeacherService

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

def test_create_teacher_with_valid_data(client):
    """Test creating a teacher with valid name and email."""
    response = client.post('/teachers', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201
    assert b'Teacher created successfully' in response.data

def test_create_teacher_with_missing_name(client):
    """Test error when creating a teacher without name."""
    response = client.post('/teachers', json={
        "email": "john.doe@example.com"
    })
    assert response.status_code == 400
    assert b'Name is required' in response.data

def test_create_teacher_with_invalid_email(client):
    """Test error when creating a teacher with invalid email format."""
    response = client.post('/teachers', json={
        "name": "John Doe",
        "email": "not-an-email"
    })
    assert response.status_code == 400
    assert b'Invalid email format' in response.data

def test_get_teacher_with_valid_id(client):
    """Test retrieving a teacher successfully."""
    teacher = Teacher(name="Jane Doe", email="jane.doe@example.com")
    TeacherService.create_teacher(teacher)  # Assuming this method saves the teacher to the DB

    response = client.get(f'/teachers/{teacher.id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == "Jane Doe"
    assert data['email'] == "jane.doe@example.com"

def test_get_teacher_with_non_existent_id(client):
    """Test error when trying to retrieve a non-existent teacher."""
    response = client.get('/teachers/999999')  # Assuming this ID does not exist
    assert response.status_code == 404
    assert b'Teacher not found' in response.data
```