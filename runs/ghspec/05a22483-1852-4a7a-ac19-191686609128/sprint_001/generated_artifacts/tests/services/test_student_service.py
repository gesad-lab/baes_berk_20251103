import pytest
from src.services.student_service import create_student, get_student_by_id
from src.models import Student
from unittest.mock import patch

@pytest.fixture
def mock_student():
    """Create mock student data for testing."""
    return Student(id=1, name="John Doe")

def test_create_student_creates_student_successfully():
    """Test creating a student successfully."""
    name = "Jane Doe"

    with patch('src.services.student_service.Student') as mock_student_class:
        mock_student_instance = mock_student_class.return_value
        mock_student_instance.save.return_value = None  # Simulates successful save operation
        
        student = create_student(name)

        assert student.name == name
        mock_student_class.assert_called_once_with(name=name)
        mock_student_instance.save.assert_called_once()

def test_get_student_by_id_returns_student(mock_student):
    """Test retrieving a student by ID successfully."""
    student_id = 1

    with patch('src.services.student_service.get_student_by_id') as mock_get_student:
        mock_get_student.return_value = mock_student
        
        student = get_student_by_id(student_id)

        assert student.id == mock_student.id
        assert student.name == mock_student.name
        mock_get_student.assert_called_once_with(student_id)

def test_get_student_by_id_returns_none_for_nonexistent_id():
    """Test retrieving a student by ID that does not exist."""
    student_id = 999  # An ID that we don't expect to exist

    with patch('src.services.student_service.get_student_by_id') as mock_get_student:
        mock_get_student.return_value = None
        
        student = get_student_by_id(student_id)

        assert student is None
        mock_get_student.assert_called_once_with(student_id)