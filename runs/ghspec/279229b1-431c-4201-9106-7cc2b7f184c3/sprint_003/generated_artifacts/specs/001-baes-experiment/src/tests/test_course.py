```python
import pytest
import json
from your_app_name import create_app, db  # Adjust according to your application structure
from your_app_name.models import Course  # Assuming Course model exists

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for tests
    with app.app_context():
        db.create_all()  # Create tables
        yield app
        db.drop_all()  # Cleanup after tests

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_course_with_valid_data(client):
    response = client.post('/courses', json={'name': 'Mathematics', 'level': '101'})
    assert response.status_code == 201

def test_create_course_without_name(client):
    response = client.post('/courses', json={'level': '101'})
    assert response.status_code == 400  # Expecting a client error for bad request
    assert response.json['error']['code'] == 'E002'
    assert response.json['error']['message'] == 'Name is required.'

def test_create_course_without_level(client):
    response = client.post('/courses', json={'name': 'Science'})
    assert response.status_code == 400  # Expecting a client error for bad request
    assert response.json['error']['code'] == 'E003'
    assert response.json['error']['message'] == 'Level is required.'

def test_get_courses(client):
    # Prepopulate with a course
    client.post('/courses', json={'name': 'Mathematics', 'level': '101'})
    response = client.get('/courses')
    assert response.status_code == 200
    assert len(response.json) == 1  # Should return one course
    assert response.json[0]['name'] == 'Mathematics'
    assert response.json[0]['level'] == '101'
```