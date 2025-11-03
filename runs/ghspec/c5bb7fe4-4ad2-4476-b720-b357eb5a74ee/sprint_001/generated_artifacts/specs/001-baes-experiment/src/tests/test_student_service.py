```python
import pytest
from src.services.student_service import create_student, get_student, update_student, delete_student
from src.models import Student
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def student_data():
    """Fixture for student data."""
    return {"name": "John Doe"}

def test_create_student(student_data):
    """Test creating a new student successfully."""
    student = create_student(student_data)
    assert isinstance(student, Student), "Should return a Student instance"
    assert student.name == student_data["name"], "Student name should match input data"

def test_create_student_without_name():
    """Test creating a student without a name raises a validation error."""
    with pytest.raises(IntegrityError):
        create_student({"name": ""})

def test_get_student(student_data):
    """Test retrieving a student by ID."""
    student = create_student(student_data)
    fetched_student = get_student(student.id)
    assert fetched_student.id == student.id, "Fetched student should have the same ID"
    assert fetched_student.name == student_data["name"], "Fetched student name should match input data"

def test_update_student(student_data):
    """Test updating an existing student's name."""
    student = create_student(student_data)
    updated_data = {"name": "Jane Doe"}
    updated_student = update_student(student.id, updated_data)
    assert updated_student.name == updated_data["name"], "Updated student name should match new data"

def test_delete_student(student_data):
    """Test deleting a student."""
    student = create_student(student_data)
    delete_student(student.id)
    assert get_student(student.id) is None, "Student should not be found after deletion"

def test_get_nonexistent_student():
    """Test fetching a nonexistent student returns None."""
    assert get_student(-1) is None, "Fetching a nonexistent student should return None"
```