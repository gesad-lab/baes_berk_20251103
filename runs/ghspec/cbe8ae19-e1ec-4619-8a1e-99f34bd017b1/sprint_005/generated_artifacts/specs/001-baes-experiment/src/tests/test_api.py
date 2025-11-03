```python
import pytest
from services.teacher_service import create_teacher, get_all_teachers
from models import db

@pytest.fixture
def setup_database():
    """Setup a test database before each test."""
    db.create_all()  # Create the database tables
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Cleanup the database

def test_create_teacher_with_invalid_email(setup_database):
    """Test creating a teacher with an invalid email format."""
    response = create_teacher({"name": "Alice Smith", "email": "invalid-email"})
    assert response["error"]["code"] == "E001"  # Assume E001 is the code for invalid email
    assert "Invalid email format" in response["error"]["message"]

def test_create_teacher_with_missing_name(setup_database):
    """Test creating a teacher with a missing name."""
    response = create_teacher({"email": "alice.smith@example.com"})
    assert response["error"]["code"] == "E002"  # Assume E002 is the code for missing name
    assert "Name is required" in response["error"]["message"]

def test_create_teacher_with_empty_fields(setup_database):
    """Test creating a teacher with empty fields."""
    response = create_teacher({"name": "", "email": ""})
    assert response["error"]["code"] == "E001"  # Assume E001 is the code for invalid email
    assert "Invalid email format" in response["error"]["message"]
    assert response["error"]["code"] == "E002"  # Code for missing/empty name
    assert "Name is required" in response["error"]["message"]

def test_create_teacher_valid_input(setup_database):
    """Test creating a teacher with valid data."""
    response = create_teacher({"name": "John Doe", "email": "john.doe@example.com"})
    assert response["message"] == "Teacher successfully created."

def test_list_teachers_empty(setup_database):
    """Test listing teachers when no teachers are present."""
    teachers = get_all_teachers()
    assert teachers == []  # No teachers should be present

def test_list_teachers_with_one_entry(setup_database):
    """Test listing teachers with a single teacher present."""
    create_teacher({"name": "John Doe", "email": "john.doe@example.com"})
    teachers = get_all_teachers()
    assert len(teachers) == 1
    assert teachers[0]["name"] == "John Doe"
    assert teachers[0]["email"] == "john.doe@example.com"
```