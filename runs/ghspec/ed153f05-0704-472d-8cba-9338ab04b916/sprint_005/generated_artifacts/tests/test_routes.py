```python
import pytest
from flask import json
from src.database import get_db, init_db
from src.models import Teacher
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test

@pytest.fixture(scope='module')
def test_client(db):
    """Create a test client for making API requests."""
    from src.app import create_app
    app = create_app()
    with app.test_client() as client:
        yield client

def test_create_teacher_valid(test_client):
    """Test creating a new teacher with valid data."""
    response = test_client.post('/teachers', json={
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    })
    assert response.status_code == 201
    assert response.get_json() == {"message": "Teacher created successfully."}

def test_create_teacher_missing_name(test_client):
    """Test creating a teacher while missing the name."""
    response = test_client.post('/teachers', json={
        "email": "jane.doe@example.com"
    })
    assert response.status_code == 400
    assert response.get_json() == {"error": {"code": "E001", "message": "Name is required."}}

def test_create_teacher_missing_email(test_client):
    """Test creating a teacher while missing the email."""
    response = test_client.post('/teachers', json={
        "name": "Jane Doe"
    })
    assert response.status_code == 400
    assert response.get_json() == {"error": {"code": "E002", "message": "Email is required."}}

def test_create_teacher_duplicate_email(test_client, db):
    """Test creating a teacher with a duplicate email."""
    test_client.post('/teachers', json={
        "name": "Jane Rogue",
        "email": "jane.rogue@example.com"
    })  # Create the first teacher

    response = test_client.post('/teachers', json={
        "name": "Jane Repeat",
        "email": "jane.rogue@example.com"
    })  # Attempt to create a second teacher with the same email
    assert response.status_code == 409  # Conflict expected for duplicate email
```
