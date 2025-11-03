```python
import pytest
from flask import json
from src.app import create_app, db
from src.models.teacher import Teacher  # Importing the Teacher model

@pytest.fixture
def app():
    """Fixture for creating a Flask application with test configuration."""
    app = create_app({'TESTING': True})

    with app.app_context():
        # Create the database and tables for Teacher
        db.create_all()
        yield app
        # Drop the database after tests are finished
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture for providing a test client for the Flask application."""
    return app.test_client()

def test_create_teacher_success(client):
    """Test case for successfully creating a new teacher."""
    response = client.post('/teachers', 
                            data=json.dumps({'name': 'John Doe', 'email': 'john.doe@example.com'}),
                            content_type='application/json')
    
    assert response.status_code == 201  # HTTP status code for Created
    assert response.json['message'] == 'Teacher created successfully'
    assert Teacher.query.filter_by(email='john.doe@example.com').first() is not None

def test_create_teacher_validation_error(client):
    """Test case for creating a teacher without required fields."""
    response = client.post('/teachers', 
                            data=json.dumps({'name': '', 'email': ''}),
                            content_type='application/json')
    
    assert response.status_code == 400  # HTTP status code for Bad Request
    assert response.json['error']['message'] == 'Both name and email are required'

def test_create_teacher_duplicate_email(client):
    """Test case for creating a teacher with a duplicate email."""
    client.post('/teachers', 
                data=json.dumps({'name': 'John Doe', 'email': 'john.doe@example.com'}),
                content_type='application/json')

    response = client.post('/teachers', 
                            data=json.dumps({'name': 'Jane Smith', 'email': 'john.doe@example.com'}),
                            content_type='application/json')

    assert response.status_code == 400  # HTTP status code for Bad Request
    assert response.json['error']['message'] == 'Email already exists'

def test_get_teacher_success(client):
    """Test case for retrieving teacher information with a valid ID."""
    teacher = Teacher(name='John Doe', email='john.doe@example.com')
    db.session.add(teacher)
    db.session.commit()

    response = client.get(f'/teachers/{teacher.id}')
    
    assert response.status_code == 200  # HTTP status code for OK
    assert response.json['name'] == 'John Doe'
    assert response.json['email'] == 'john.doe@example.com'

def test_get_teacher_not_found(client):
    """Test case for retrieving teacher information with an invalid ID."""
    response = client.get('/teachers/999999')  # Assuming this ID doesn't exist
    
    assert response.status_code == 404  # HTTP status code for Not Found
    assert response.json['error']['message'] == 'Teacher not found'
```