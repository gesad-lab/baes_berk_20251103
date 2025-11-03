```python
import pytest
from src.database import get_db, init_db
from src.app import create_app
from src.models import Student

@pytest.fixture
def app():
    """Create a new Flask application instance for testing."""
    app = create_app({"TESTING": True})
    with app.app_context():
        init_db()  # Initialize the database with the schema
    yield app

@pytest.fixture
def client(app):
    """Create a test client for the application."""
    return app.test_client()

def test_create_student_with_valid_email(client):
    """Test that creating a student with a valid email is successful."""
    response = client.post('/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201  # Check for successful creation
    data = response.get_json()
    assert 'id' in data  # Ensure an ID is returned
    assert data['name'] == "John Doe"
    assert data['email'] == "john.doe@example.com"

def test_invalid_email_format(client):
    """Test that an invalid email format results in a 400 error."""
    response = client.post('/students', json={
        "name": "Jane Doe",
        "email": "invalid-email"
    })
    assert response.status_code == 400  # Check for bad request
    error_data = response.get_json()
    assert 'error' in error_data  # Ensure error message is present
    assert error_data['error']['message'] == "Email is required and must be in a valid format."  # Check for correct error message
```