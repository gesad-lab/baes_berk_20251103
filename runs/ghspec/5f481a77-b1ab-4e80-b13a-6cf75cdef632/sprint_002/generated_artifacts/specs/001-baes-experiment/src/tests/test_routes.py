```python
import pytest
from flask import json
from src.app import app  # Assuming the Flask app is initialized in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_student_with_valid_email(client):
    response = client.post('/students', data=json.dumps({
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }), content_type='application/json')
    
    assert response.status_code == 201  # Check if student was created successfully
    assert response.json['email'] == 'john.doe@example.com'  # Check if the email was saved correctly

def test_add_student_with_invalid_email(client):
    response = client.post('/students', data=json.dumps({
        'name': 'Jane Doe',
        'email': 'invalid-email'
    }), content_type='application/json')
    
    assert response.status_code == 400  # Check if the appropriate error response is returned
    assert 'error' in response.json  # Validate that an error is present in the response
    assert response.json['error']['code'] == 'E001'  # Assuming E001 is the error code for invalid email format
    assert 'message' in response.json['error']  # Ensure that a meaningful message is provided

def test_add_student_without_email(client):
    response = client.post('/students', data=json.dumps({
        'name': 'Missing Email'
    }), content_type='application/json')
    
    assert response.status_code == 400  # Check if the appropriate error response is returned
    assert 'error' in response.json  # Validate that an error is present in the response
    assert response.json['error']['code'] == 'E002'  # Assuming E002 is the error code for missing required field
    assert 'message' in response.json['error']  # Ensure that a meaningful message is provided
```