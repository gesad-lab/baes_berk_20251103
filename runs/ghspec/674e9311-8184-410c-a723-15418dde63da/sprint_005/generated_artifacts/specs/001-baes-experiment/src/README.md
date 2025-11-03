```python
import pytest
from flask import Flask, jsonify
from src.api import create_app
from src.models.teacher import Teacher  # Importing the Teacher model
from src.models import db  # Assuming db is imported correctly for testing
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def app():
    # Set up the Flask app for testing
    app = create_app()  # Assuming create_app initializes the Flask app
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for tests
    with app.app_context():
        db.create_all()  # Create all tables
        yield app  # Yield the app to the test functions
        db.drop_all()  # Clean up after tests

@pytest.fixture
def client(app):
    return app.test_client()

def test_retrieve_all_teachers(client):
    # Given: there are teachers already created
    teacher1 = Teacher(name="Jane Doe", email="jane.doe@example.com")
    teacher2 = Teacher(name="John Smith", email="john.smith@example.com")
    
    # Add to the session and commit
    with app.app_context():
        db.session.add(teacher1)
        db.session.add(teacher2)
        db.session.commit()
    
    # When: an administrator requests to view the list of teachers
    response = client.get('/teachers')

    # Then: the system should return a JSON response containing details of all the teachers
    assert response.status_code == 200
    json_data = response.get_json()
    
    # Check if the response contains the correct teacher details
    assert isinstance(json_data, list)  # Ensure it's a list
    assert len(json_data) == 2  # Ensure we get back 2 teachers
    assert any(teacher['name'] == "Jane Doe" for teacher in json_data)
    assert any(teacher['email'] == "jane.doe@example.com" for teacher in json_data)
    assert any(teacher['name'] == "John Smith" for teacher in json_data)
    assert any(teacher['email'] == "john.smith@example.com" for teacher in json_data)
```