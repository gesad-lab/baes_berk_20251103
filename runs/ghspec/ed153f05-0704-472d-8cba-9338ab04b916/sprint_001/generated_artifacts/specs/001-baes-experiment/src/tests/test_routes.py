```python
import pytest
from flask import json
from src.app import create_app
from src.database import db
from src.models import Student

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()  # Create tables in the test database
    yield app.test_client()
    with app.app_context():
        db.drop_all()  # Clean up after tests


def test_create_student(client):
    """Test the creation of a new student."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201  # HTTP status 201 Created
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'
    assert 'id' in data  # Check that an ID is returned


def test_retrieve_student_by_id(client):
    """Test retrieval of a student by ID."""
    student = Student(name='Jane Doe')
    db.session.add(student)
    db.session.commit()

    response = client.get(f'/students/{student.id}')
    assert response.status_code == 200  # HTTP status 200 OK
    data = json.loads(response.data)
    assert data['name'] == 'Jane Doe'


def test_retrieve_all_students(client):
    """Test retrieval of all students."""
    db.session.add(Student(name='Alice'))
    db.session.add(Student(name='Bob'))
    db.session.commit()

    response = client.get('/students')
    assert response.status_code == 200  # HTTP status 200 OK
    data = json.loads(response.data)
    assert len(data) == 2  # Check that we have two students


def test_validation_of_missing_name(client):
    """Test handling of missing 'name' in student creation."""
    response = client.post('/students', json={})
    assert response.status_code == 400  # HTTP status 400 Bad Request
    data = json.loads(response.data)
    assert data['error']['message'] == "'name' is required"  # Check error message
```