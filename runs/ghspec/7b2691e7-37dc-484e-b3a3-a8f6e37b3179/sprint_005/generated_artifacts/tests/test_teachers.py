```python
import pytest
from flask import Flask, jsonify
from extensions import db
from models.teacher import Teacher  # Assuming this is where the Teacher model is located
from api.routes.teachers import teachers_bp  # Assuming the teachers API is set up in this module

@pytest.fixture
def app():
    """Create a new Flask application instance for testing."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
    app.register_blueprint(teachers_bp)  # Register the teachers blueprint
    with app.app_context():
        db.create_all()  # Create all tables in the in-memory database
    yield app  # This will allow tests to run

@pytest.fixture
def client(app):
    """Create a test client for the Flask app."""
    return app.test_client()

def test_create_teacher(client):
    """Test the creation of a new teacher."""
    response = client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201
    response_data = response.get_json()
    assert response_data['name'] == 'John Doe'
    assert response_data['email'] == 'john.doe@example.com'

def test_retrieve_teachers(client):
    """Test retrieving all teachers."""
    client.post('/teachers', json={
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com'
    })
    response = client.get('/teachers')
    assert response.status_code == 200
    response_data = response.get_json()
    assert len(response_data) == 1
    assert response_data[0]['name'] == 'Jane Smith'
    assert response_data[0]['email'] == 'jane.smith@example.com'

def test_create_teacher_with_missing_name(client):
    """Test creating a teacher without a name."""
    response = client.post('/teachers', json={
        'email': 'missing.name@example.com'
    })
    assert response.status_code == 400
    response_data = response.get_json()
    assert response_data['error']['code'] == 'E001'
    assert 'name' in response_data['error']['details']

def test_create_teacher_with_invalid_email(client):
    """Test creating a teacher with an invalid email."""
    response = client.post('/teachers', json={
        'name': 'Invalid Email',
        'email': 'not-an-email'
    })
    assert response.status_code == 400
    response_data = response.get_json()
    assert response_data['error']['code'] == 'E002'
    assert 'email' in response_data['error']['details']
```