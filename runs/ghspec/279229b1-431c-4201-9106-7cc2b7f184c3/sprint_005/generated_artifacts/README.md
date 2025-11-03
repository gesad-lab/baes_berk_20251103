```python
import pytest
import json
from your_app_name import create_app, db
from your_app_name.models import Teacher  # Assuming Teacher model exists

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create database tables in memory
        yield client
        db.drop_all()  # Clean up after tests

def test_create_teacher(client):
    """Test successful teacher creation"""
    response = client.post('/teachers', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 200
    assert response.json['message'] == "Teacher created successfully."

def test_create_teacher_missing_name(client):
    """Test teacher creation attempt without a name"""
    response = client.post('/teachers', json={'email': 'john.doe@example.com'})
    assert response.json['error']['code'] == 'E001'  # E001: Missing name

def test_create_teacher_missing_email(client):
    """Test teacher creation attempt without an email"""
    response = client.post('/teachers', json={'name': 'John Doe'})
    assert response.json['error']['code'] == 'E002'  # E002: Missing email
```