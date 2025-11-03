import pytest
import json
from your_app_name import create_app, db  # Adjust according to your application structure
from your_app_name.models import Course  # Adjust according to your application structure

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for tests
    with app.app_context():
        db.create_all()  # Create tables
        yield app
        db.drop_all()  # Clean up after tests

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_course_with_valid_data(client):
    """Tests that a course can be created with valid data."""
    response = client.post('/courses', json={'name': 'Mathematics', 'level': '101'})
    assert response.status_code == 201
    assert response.json['name'] == 'Mathematics'
    assert response.json['level'] == '101'

def test_create_course_without_name(client):
    """Tests that creating a course without a name returns an error."""
    response = client.post('/courses', json={'level': '101'})
    assert response.status_code == 400  # Assuming 400 for bad request
    assert response.json['error']['code'] == 'E002'  # Error code for missing name

def test_create_course_without_level(client):
    """Tests that creating a course without a level returns an error."""
    response = client.post('/courses', json={'name': 'Mathematics'})
    assert response.status_code == 400  # Assuming 400 for bad request
    assert response.json['error']['code'] == 'E003'  # Error code for missing level

def test_retrieve_courses(client):
    """Tests that retrieving courses returns a list of courses formatted as JSON."""
    # First, create some courses
    client.post('/courses', json={'name': 'Mathematics', 'level': '101'})
    client.post('/courses', json={'name': 'Physics', 'level': '102'})
    
    response = client.get('/courses')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Should return a JSON list
    assert len(response.json) == 2  # We expect 2 courses
    assert response.json[0]['name'] == 'Mathematics'
    assert response.json[0]['level'] == '101'
    assert response.json[1]['name'] == 'Physics'
    assert response.json[1]['level'] == '102'