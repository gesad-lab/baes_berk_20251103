```python
import pytest
from app import create_app, db
from app.models import Student

@pytest.fixture
def client():
    """A test client for the Flask application."""
    app = create_app('testing')  # Use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database after tests

def test_create_student_with_email(client):
    """Test creating a student with a valid name and email."""
    response = client.post('/students', json={"name": "Test Student", "email": "test@example.com"})
    assert response.status_code == 201
    # Verify the student was created successfully in the database
    student = Student.query.filter_by(email="test@example.com").first()
    assert student is not None
    assert student.name == "Test Student"
    assert student.email == "test@example.com"

def test_retrieve_students(client):
    """Test retrieving all students including their emails."""
    client.post('/students', json={"name": "Test Student", "email": "test@example.com"})
    response = client.get('/students')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # Ensure response is a list
    assert len(data) > 0  # Check that there is at least one student
    assert 'name' in data[0] and 'email' in data[0]  # Check that email field is present

def test_update_student_email(client):
    """Test updating a student's email."""
    response = client.post('/students', json={"name": "Test Student", "email": "test@example.com"})
    student_id = response.get_json()['id']
    response = client.put(f'/students/{student_id}', json={"email": "updated@example.com"})
    assert response.status_code == 200
    updated_student = Student.query.get(student_id)
    assert updated_student.email == "updated@example.com"  # Check that the email was updated

def test_create_student_without_email_fails(client):
    """Test that creating a student without an email fails."""
    response = client.post('/students', json={"name": "Test Student"})
    assert response.status_code == 400  # Bad Request
    assert 'error' in response.get_json()  # Ensure an error message is returned

def test_existing_students_have_email_field(client):
    """Test ensuring existing students have email field present after migration."""
    # Assuming existing migration has run and students already exist before this test
    response = client.get('/students')
    assert response.status_code == 200
    data = response.get_json()
    # Check that every student record includes an email field
    for student in data:
        assert 'email' in student  # Email field should be present (may be empty)
```