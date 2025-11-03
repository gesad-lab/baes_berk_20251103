```python
import pytest
from app import create_app, db
from models import Teacher  # Assume Teacher model will be defined in models/teacher.py
from services.teacher_service import create_teacher, get_all_teachers

@pytest.fixture
def setup_database():
    """Setup a test database before each test."""
    db.create_all()  # Create the database tables
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Drop all tables after tests

def test_create_teacher_with_valid_data(setup_database):
    """Test that a teacher can be created successfully with valid data."""
    response = create_teacher(name="John Doe", email="john.doe@example.com")
    assert response["message"] == "Teacher created successfully"
    assert response["teacher"]["name"] == "John Doe"
    assert response["teacher"]["email"] == "john.doe@example.com"

def test_create_teacher_with_invalid_email(setup_database):
    """Test that an error is raised when an invalid email is provided."""
    response = create_teacher(name="Jane Doe", email="invalid-email")
    assert response["error"]["code"] == "E001"
    assert response["error"]["message"] == "Invalid email format"

def test_create_teacher_with_missing_name(setup_database):
    """Test that an error is raised when the name is missing."""
    response = create_teacher(name="", email="jane.doe@example.com")
    assert response["error"]["code"] == "E002"
    assert response["error"]["message"] == "Name is required"

def test_get_all_teachers(setup_database):
    """Test retrieving a list of all teachers."""
    create_teacher(name="Alice Smith", email="alice.smith@example.com")
    create_teacher(name="Bob Johnson", email="bob.johnson@example.com")

    teachers = get_all_teachers()
    assert len(teachers) == 2
    assert teachers[0]["name"] == "Alice Smith"
    assert teachers[1]["name"] == "Bob Johnson"
```