```python
import pytest
import json
from your_app_name import create_app, db  # Adjust according to your application structure
from your_app_name.models import Student  # Adjust according to your application structure

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

def test_update_student_email_with_invalid_format(client):
    # Step 1: First, create a student with a valid email
    response = client.post('/students', json={'name': 'Alice', 'email': 'alice@example.com'})
    assert response.status_code == 201

    # Step 2: Attempt to update the student's email to an invalid format
    student_id = response.json['id']  # Get the id of the newly created student
    invalid_email_response = client.put(f'/students/{student_id}', json={'email': 'invalid_email_format'})
    
    # Step 3: Assert that the response indicates the email format is invalid
    assert invalid_email_response.status_code == 400  # Assuming 400 is the status code for bad request
    assert invalid_email_response.json['error']['code'] == 'E002'  # Assuming E002 is the code for invalid email format
    assert 'email format is invalid' in invalid_email_response.json['error']['message']  # Check if the message is informative and actionable

def test_update_student_email_without_email(client):
    # Step 1: First, create a student with a valid email
    response = client.post('/students', json={'name': 'Bob', 'email': 'bob@example.com'})
    assert response.status_code == 201

    # Step 2: Attempt to update the student's email without providing an email
    student_id = response.json['id']  # Get the id of the newly created student
    no_email_response = client.put(f'/students/{student_id}', json={})
    
    # Step 3: Assert that the response indicates the email field is required
    assert no_email_response.status_code == 400  # Assuming 400 is the status code for bad request
    assert no_email_response.json['error']['code'] == 'E001'  # Assuming E001 is the code for required field
    assert 'email field is required' in no_email_response.json['error']['message']  # Check for informative message
```