```python
import pytest
import json

# Sample data for testing
students = []

@pytest.fixture
def client():
    from main import app  # Assuming your Flask app is in main.py
    with app.test_client() as client:
        yield client

@pytest.fixture
def valid_student_data():
    """Provides valid student data including name and email for creating a new student."""
    return {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }

@pytest.fixture
def invalid_email_data():
    """Provides invalid email data for testing email validation."""
    return {
        "name": "Invalid Email",
        "email": "invalid-email"
    }

def test_create_student_success(client, valid_student_data):
    response = client.post('/students', json=valid_student_data)
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['name'] == valid_student_data['name']
    assert response.json['email'] == valid_student_data['email']

def test_create_student_missing_name(client):
    response = client.post('/students', json={'email': 'test@example.com'})
    assert response.status_code == 400  # Bad Request for missing name
    assert response.json['error']['code'] == 'E001'
    assert response.json['error']['message'] == 'Missing required field: name'

def test_create_student_invalid_email(client, invalid_email_data):
    response = client.post('/students', json=invalid_email_data)
    assert response.status_code == 400  # Bad Request for invalid email
    assert response.json['error']['code'] == 'E002'
    assert response.json['error']['message'] == 'Invalid email format'

def test_get_student_by_id(client, valid_student_data):
    # Create a student to retrieve
    create_response = client.post('/students', json=valid_student_data)
    student_id = create_response.json['id']
    
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json['name'] == valid_student_data['name']
    assert response.json['email'] == valid_student_data['email']

def test_update_student_email_success(client, valid_student_data):
    # Create a student to update
    create_response = client.post('/students', json=valid_student_data)
    student_id = create_response.json['id']

    # Update the student's email
    updated_data = {"email": "jane.new@example.com"}
    response = client.put(f'/students/{student_id}', json=updated_data)
    assert response.status_code == 200
    assert response.json['email'] == updated_data['email']

def test_update_student_with_invalid_email(client, valid_student_data):
    # Create a student to update
    create_response = client.post('/students', json=valid_student_data)
    student_id = create_response.json['id']

    # Attempt to update with invalid email
    updated_data = {"email": "invalid-email"}
    response = client.put(f'/students/{student_id}', json=updated_data)
    assert response.status_code == 400  # Bad Request for invalid email
    assert response.json['error']['code'] == 'E002'
    assert response.json['error']['message'] == 'Invalid email format'
```