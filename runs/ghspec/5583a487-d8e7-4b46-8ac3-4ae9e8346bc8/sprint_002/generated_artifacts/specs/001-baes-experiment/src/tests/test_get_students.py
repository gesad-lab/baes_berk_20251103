```python
import pytest
from flask import jsonify
from app import app, db, Student  # Import the app and models from the main application

# Setup the Flask application for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Cleanup database after tests    

def test_get_students_empty(client):
    """Test retrieving students when no records exist."""
    response = client.get('/students')
    assert response.status_code == 200
    assert response.json == []  # Expected empty list if no students exist

def test_get_students_with_records(client):
    """Test retrieving students returns correct records with email."""
    # Arrange: Create a sample student record with name and email
    new_student = Student(name='Jane Doe', email='jane@example.com')
    db.session.add(new_student)
    db.session.commit()
    
    # Act: Retrieve the student records
    response = client.get('/students')
    
    # Assert: Check if the response contains the correct student data
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'Jane Doe'
    assert response.json[0]['email'] == 'jane@example.com'  # Ensure email is included

def test_get_students_invalid_email_format(client):
    """Test retrieving students with an invalid email format returns appropriate error."""
    # Arrange: Try to create a student with an invalid email
    invalid_student_data = {'name': 'John Doe', 'email': 'not-an-email'}
    response = client.post('/students', json=invalid_student_data)
    
    # Assert: Check that the request fails due to email validation
    assert response.status_code == 400
    assert 'Invalid email format' in response.json['message']  # Check for specific error message
```