```python
import pytest
from src.app import app, db
from src.models import Student

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_create_student(client):
    """Test that a student can be created successfully."""
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john@example.com'})
    assert response.status_code == 201  # Ensure creation is successful
    assert response.json == {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}  # Check response

def test_create_student_missing_email(client):
    """Test that a validation error is returned when email is not provided."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 400  # Ensure bad request for missing email
    assert response.json == {
        "error": {
            "code": "E001",
            "message": "Email is required.",
            "details": {}
        }
    }  # Check the error response
```