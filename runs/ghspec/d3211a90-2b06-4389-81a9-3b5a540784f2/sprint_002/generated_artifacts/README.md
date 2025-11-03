```python
import json
import pytest
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Import the application and database
from src.controllers.student_controller import app, db
from src.models.student import Student

# Test configuration
@pytest.fixture(scope='module')
def test_client():
    """Set up the test client and the database for testing."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()  # Create the database tables
        yield app.test_client()  # Provide the test client


@pytest.fixture(scope='function')
def init_database(test_client):
    """Initialize the database before each test."""
    # Create a sample student entry
    student = Student(name="John Doe", email="john.doe@example.com")
    db.session.add(student)
    db.session.commit()

    yield  # This is where the testing happens

    # Teardown: Remove all records after each test
    db.session.remove()
    db.drop_all()


def test_create_student_with_email(test_client, init_database):
    """Test the creation of a student with an email."""
    student_data = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
    
    response = test_client.post('/students', data=json.dumps(student_data), content_type='application/json')
    
    assert response.status_code == 201  # Assert the response status is Created
    response_data = json.loads(response.data)
    assert response_data['email'] == student_data['email']  # Assert the email is correctly stored


def test_get_student_with_email(test_client, init_database):
    """Test retrieving a student includes their email."""
    response = test_client.get('/students/1')  # Get the student with ID 1
    
    assert response.status_code == 200  # Assert the response status is OK
    response_data = json.loads(response.data)
    assert 'email' in response_data  # Assert email is included in the response
    assert response_data['email'] == "john.doe@example.com"  # Check the email matches expected value
```