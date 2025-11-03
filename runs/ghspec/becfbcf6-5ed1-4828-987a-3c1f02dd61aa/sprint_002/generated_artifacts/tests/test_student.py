```python
import pytest
from app import app, db, Student

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for testing
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after the tests

def test_create_student_with_valid_email(client):
    """Test that creating a student with a valid email succeeds."""
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 201  # Check for 201 Created
    data = response.get_json()
    assert 'id' in data  # Check that the response contains the student ID
    assert data['email'] == 'john.doe@example.com'  # Verify email in the response

def test_create_student_missing_email(client):
    """Test that creating a student without an email returns an error."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 400  # Check for 400 Bad Request
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Check for specific error code
    assert data['error']['message'] == 'Email field is required.'  # Check message details

def test_create_student_with_invalid_email(client):
    """Test that creating a student with an invalid email returns an error."""
    response = client.post('/students', json={'name': 'John Doe', 'email': 'invalid-email'})
    assert response.status_code == 400  # Check for 400 Bad Request
    data = response.get_json()
    assert data['error']['code'] == 'E002'  # Check for specific error code related to invalid email
    assert data['error']['message'] == 'Invalid email format.'  # Check message details
```