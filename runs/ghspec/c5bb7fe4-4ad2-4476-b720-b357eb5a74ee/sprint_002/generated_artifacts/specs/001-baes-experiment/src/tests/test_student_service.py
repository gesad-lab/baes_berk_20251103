```python
import pytest
from src.services.student_service import create_student, update_student
from src.models import Student
from sqlalchemy.exc import IntegrityError
import re

@pytest.fixture
def student_data():
    """Fixture for student data."""
    return {"name": "John Doe", "email": "john.doe@example.com"}

def test_create_student_with_valid_email(student_data):
    """Test creating a new student successfully with a valid email."""
    student = create_student(student_data)
    assert isinstance(student, Student), "Should return a Student instance"
    assert student.name == student_data["name"], "Student name should match"
    assert student.email == student_data["email"], "Student email should match"

def test_create_student_with_invalid_email(student_data):
    """Test creating a new student fails with an invalid email."""
    student_data["email"] = "invalid-email"
    with pytest.raises(IntegrityError):
        create_student(student_data)

def test_update_student_email(student_data):
    """Test updating an existing student's email."""
    student = create_student(student_data)
    new_email = "john.new@example.com"
    updated_student = update_student(student.id, {"email": new_email})
    
    assert updated_student.email == new_email, "Email should be updated"
    
def test_update_student_with_invalid_email(student_data):
    """Test updating a student's email with an invalid email fails."""
    student = create_student(student_data)
    with pytest.raises(IntegrityError):
        update_student(student.id, {"email": "invalid-email"})
```