```python
import json
import pytest
from app import app, db, Student

# Fixture to set up the test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_add_student_with_valid_name(client):
    """Test adding a student with a valid name"""
    response = client.post('/students', json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['name'] == "John Doe"
    assert data['email'] == "john@example.com"

def test_retrieve_all_students(client):
    """Test retrieving all students with their emails"""
    client.post('/students', json={"name": "John Doe", "email": "john@example.com"})
    client.post('/students', json={"name": "Jane Doe", "email": "jane@example.com"})
    
    response = client.get('/students')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2  # Should return two students
    assert any(student['email'] == "john@example.com" for student in data)
    assert any(student['email'] == "jane@example.com" for student in data)

def test_add_student_with_empty_email(client):
    """Test adding a student with an empty email field"""
    response = client.post('/students', json={"name": "John Doe", "email": ""})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == "E001"  # Assuming a specific error code for email validation
    assert data['error']['message'] == "Email field is required."

def test_add_student_with_invalid_email_format(client):
    """Test adding a student with an improperly formatted email address"""
    response = client.post('/students', json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == "E002"  # Assuming a specific error code for invalid email format
    assert data['error']['message'] == "Invalid email format."
```