```python
import pytest
from flask import json
from app import create_app, db  # Assuming create_app sets up the Flask app and db is the SQLAlchemy instance
from app.models import Student  # Assuming the Student model is defined in models.py

@pytest.fixture
def client():
    app = create_app({'TESTING': True})  # Create a test instance of the application
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
        yield client
    with app.app_context():
        db.drop_all()  # Drop all tables after tests

def test_get_all_students_empty(client):
    """Verify that retrieving all students returns an empty list when there are no records."""
    response = client.get('/students')
    assert response.status_code == 200
    assert json.loads(response.data) == []  # Assert that the received data is an empty list

def test_get_all_students_with_records(client):
    """Verify that all stored student records are retrieved correctly."""
    # Create a sample student entry
    student_data = json.dumps({"name": "John Doe"})
    client.post('/students', data=student_data, content_type='application/json')

    response = client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1  # We expect one record
    assert data[0]["name"] == "John Doe"  # Check that the name is correct

def test_get_all_students_multiple_records(client):
    """Verify that retrieving all students returns all records."""
    student_data_one = json.dumps({"name": "Alice Smith"})
    student_data_two = json.dumps({"name": "Bob Johnson"})
    client.post('/students', data=student_data_one, content_type='application/json')
    client.post('/students', data=student_data_two, content_type='application/json')

    response = client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2  # We expect two records
    assert {student['name'] for student in data} == {"Alice Smith", "Bob Johnson"}

def test_create_student_with_empty_name(client):
    """Verify that an error is returned when trying to create a student with an empty name."""
    response = client.post('/students', data=json.dumps({"name": ""}), content_type='application/json')
    assert response.status_code == 400
    error_data = json.loads(response.data)
    assert error_data == {"error": {"code": "E001", "message": "Name is required."}}  # Assert the error structure
```