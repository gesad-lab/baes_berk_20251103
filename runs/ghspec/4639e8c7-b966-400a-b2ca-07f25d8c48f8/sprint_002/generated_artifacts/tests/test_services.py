```python
import pytest
from src.app import create_app  # Assuming you have a Flask application factory
from email_validator import validate_email, EmailNotValidError

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_student_with_valid_email(client):
    """Test that creating a student with a valid email succeeds."""
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 201  # Assuming 201 Created for successful student creation

def test_create_student_with_empty_email(client):
    """Test that creating a student with an empty email returns an error."""
    response = client.post('/students', json={'name': 'Jane Doe', 'email': ''})
    assert response.status_code == 400  # Assuming 400 Bad Request for invalid emails
    assert response.json['error']['code'] == 'E001'  # Specific error code for empty email

def test_create_student_with_invalid_email_format(client):
    """Test that creating a student with an invalid email format returns an error."""
    response = client.post('/students', json={'name': 'Bob Smith', 'email': 'not-an-email'})
    assert response.status_code == 400  # Assuming 400 Bad Request for invalid emails
    assert response.json['error']['code'] == 'E002'  # Specific error code for invalid email format

# Additional tests can be added as necessary to cover edge cases and other scenarios
```