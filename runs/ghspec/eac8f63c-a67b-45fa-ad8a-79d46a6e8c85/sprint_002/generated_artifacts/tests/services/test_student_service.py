```python
import pytest
from unittest.mock import patch, MagicMock
from src.services.student_service import StudentService
from src.models.student import Student

@pytest.fixture
def student_service():
    return StudentService()

@pytest.fixture
def mock_student():
    return Student(id=1, name='John Doe', age=20, email='john.doe@example.com')

def test_add_student_success(student_service, mock_student):
    """Test adding a new student successfully."""
    with patch('src.repositories.student_repository.add_student', return_value=mock_student) as mock_add:
        result = student_service.add_student(mock_student)
        mock_add.assert_called_once_with(mock_student)
        assert result == mock_student

def test_add_student_missing_email(student_service, mock_student):
    """Test adding a student with missing email raises ValueError."""
    student_without_email = Student(id=2, name='Jane Doe', age=22, email=None)

    with pytest.raises(ValueError) as exc_info:
        student_service.add_student(student_without_email)
    assert str(exc_info.value) == "Email must be provided."

def test_add_student_invalid_email_format(student_service, mock_student):
    """Test adding a student with an invalid email format raises ValueError."""
    student_with_invalid_email = Student(id=3, name='Mark Smith', age=21, email='invalid-email')

    with pytest.raises(ValueError) as exc_info:
        student_service.add_student(student_with_invalid_email)
    assert str(exc_info.value) == "Invalid email format."

def test_add_student_error_handling(student_service, mock_student):
    """Test handling of error when adding a student fails."""
    with patch('src.repositories.student_repository.add_student', side_effect=Exception("Database error")):
        with pytest.raises(Exception) as exc_info:
            student_service.add_student(mock_student)
        assert str(exc_info.value) == "Database error"
```