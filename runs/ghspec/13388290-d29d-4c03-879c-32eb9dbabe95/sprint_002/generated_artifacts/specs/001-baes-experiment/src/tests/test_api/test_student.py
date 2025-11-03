```python
import pytest
from app import create_app, db
from app.models import Student
from http import HTTPStatus

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the schema for testing
            # Create a sample student for testing retrieval
            new_student = Student(name="Test Student", email="test@student.com")
            db.session.add(new_student)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_get_student_by_id_includes_email(client):
    """Test retrieval of a student by ID includes the email in the response."""
    # Assuming we created a student with ID 1 during the fixture setup
    response = client.get('/students/1')
    assert response.status_code == HTTPStatus.OK
    data = response.get_json()
    assert data['id'] == 1
    assert 'email' in data  # Check if email is included
    assert data['email'] == "test@student.com"  # Validate email retrieved

def test_get_student_with_invalid_id(client):
    """Test retrieval of a student with a non-existent ID returns a 404 error."""
    response = client.get('/students/9999')  # Assuming this ID does not exist
    assert response.status_code == HTTPStatus.NOT_FOUND
    error_data = response.get_json()
    assert error_data['error']['code'] == 'E404'
    assert error_data['error']['message'] == 'Student not found'  # Assuming this error format

def test_get_student_without_email(client):
    """Test retrieving a student record that doesn't have an email."""
    # Create another student without an email
    new_student = Student(name="No Email Student", email=None)
    db.session.add(new_student)
    db.session.commit()

    response = client.get('/students/2')  # This ID corresponds to the new student
    assert response.status_code == HTTPStatus.OK
    data = response.get_json()
    assert data['id'] == 2
    assert 'email' in data  # Email key should exist
    assert data['email'] is None  # Validate email is None (or use an empty string based on your model)
```