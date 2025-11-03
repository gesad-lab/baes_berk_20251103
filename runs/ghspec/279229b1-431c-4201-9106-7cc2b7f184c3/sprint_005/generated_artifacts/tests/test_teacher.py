```python
import pytest
import json
from your_app_name import create_app, db  # Adjust according to your application structure
from your_app_name.models import Teacher  # Import new Teacher model

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
    with app.app_context():
        db.create_all()  # Create all tables, including Teacher
        yield app
        db.drop_all()  # Clean up after tests

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_teacher_with_valid_data(client):
    response = client.post('/teachers', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 201  # 201 Created
    assert response.json == {'message': 'Teacher created successfully'}

def test_create_teacher_without_name(client):
    response = client.post('/teachers', json={'email': 'john.doe@example.com'})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json == {'error': {'code': 'E001', 'message': 'Name is required.'}}

def test_create_teacher_without_email(client):
    response = client.post('/teachers', json={'name': 'John Doe'})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json == {'error': {'code': 'E002', 'message': 'Email is required.'}}

def test_teacher_table_creation(client):
    # Assert that the Teacher table exists in the database
    with client.application.app_context():
        assert db.engine.has_table('teachers')

```