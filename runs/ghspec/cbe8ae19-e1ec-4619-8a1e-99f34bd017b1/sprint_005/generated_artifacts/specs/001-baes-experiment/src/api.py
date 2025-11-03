```python
# tests/test_teacher_service.py
import pytest
from models import db, Teacher
from services.teacher_service import create_teacher, get_teacher_by_id

@pytest.fixture
def setup_database():
    """Setup a test database before each test."""
    db.create_all()  # Create the database tables
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Drop all tables after tests

def test_create_teacher(setup_database):
    """Test the creation of a new teacher entity."""
    teacher_data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    
    # Create a new teacher and verify the result
    teacher = create_teacher(**teacher_data)
    assert teacher.id is not None  # Ensure the teacher has an ID
    assert teacher.name == 'John Doe'  # Verify the name
    assert teacher.email == 'john.doe@example.com'  # Verify the email

def test_get_teacher_by_id(setup_database):
    """Test retrieving a teacher by ID."""
    teacher_data = {
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com'
    }
    
    # Create a new teacher
    teacher = create_teacher(**teacher_data)
    
    # Attempt to retrieve the teacher by ID
    fetched_teacher = get_teacher_by_id(teacher.id)
    assert fetched_teacher is not None  # Ensure the teacher is found
    assert fetched_teacher.id == teacher.id  # Verify the ID matches
    assert fetched_teacher.name == 'Jane Smith'  # Verify the name matches

def test_create_teacher_with_invalid_email(setup_database):
    """Test the creation of a teacher with an invalid email."""
    teacher_data = {
        'name': 'Invalid Email',
        'email': 'invalid-email-format'
    }
    
    # Attempt to create a teacher and expect an error
    with pytest.raises(ValueError, match="Invalid email format"):
        create_teacher(**teacher_data)

def test_get_teacher_by_non_existent_id(setup_database):
    """Test retrieving a teacher by a nonexistent ID."""
    fetched_teacher = get_teacher_by_id(999)  # Assuming this ID doesn't exist
    assert fetched_teacher is None  # Ensure no teacher is found
```