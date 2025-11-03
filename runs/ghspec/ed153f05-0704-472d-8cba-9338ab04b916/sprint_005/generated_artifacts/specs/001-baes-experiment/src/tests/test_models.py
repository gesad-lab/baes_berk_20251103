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

def test_create_teacher_valid(db):
    """Test creating a new teacher with valid data."""
    response = db.post('/teachers', json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201
    assert response.json == {"message": "Teacher created successfully."}
    
    # Verify that the teacher was actually created in the database
    teachers = Teacher.query.all()
    assert len(teachers) == 1
    assert teachers[0].name == "Jane Doe"
    assert teachers[0].email == "jane.doe@example.com"

def test_create_teacher_missing_name(db):
    """Test creating a teacher with missing name returns error."""
    response = db.post('/teachers', json={"email": "jane.doe@example.com"})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E001", "message": "Name is required."}}

def test_create_teacher_missing_email(db):
    """Test creating a teacher with missing email returns error."""
    response = db.post('/teachers', json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E002", "message": "Email is required."}}

def test_create_teacher_duplicate_email(db):
    """Test creating a teacher with duplicate email raises IntegrityError."""
    db.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    with pytest.raises(IntegrityError):
        db.post('/teachers', json={"name": "Jane Doe", "email": "john.doe@example.com"})
```