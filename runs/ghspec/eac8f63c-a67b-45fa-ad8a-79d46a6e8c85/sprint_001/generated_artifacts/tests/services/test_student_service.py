import pytest
from unittest.mock import patch, MagicMock
from src.services.student_service import StudentService
from src.models.student import Student

@pytest.fixture
def student_service():
    return StudentService()

@pytest.fixture
def mock_student():
    return Student(id=1, name='John Doe', age=20)

def test_add_student_success(student_service, mock_student):
    """Test adding a new student successfully."""
    with patch('src.repositories.student_repository.add_student', return_value=mock_student) as mock_add:
        result = student_service.add_student(mock_student)
        mock_add.assert_called_once_with(mock_student)
        assert result == mock_student

def test_add_student_failure(student_service):
    """Test adding a student fails when repository raises an error."""
    with patch('src.repositories.student_repository.add_student', side_effect=Exception("DB error")):
        with pytest.raises(Exception) as exc_info:
            student_service.add_student(Student(name='Invalid Student', age=20))
        assert str(exc_info.value) == "DB error"

def test_get_student_success(student_service, mock_student):
    """Test retrieving a student successfully by ID."""
    with patch('src.repositories.student_repository.get_student_by_id', return_value=mock_student) as mock_get:
        result = student_service.get_student(1)
        mock_get.assert_called_once_with(1)
        assert result == mock_student

def test_get_student_not_found(student_service):
    """Test retrieving a student that does not exist."""
    with patch('src.repositories.student_repository.get_student_by_id', return_value=None):
        result = student_service.get_student(999)
        assert result is None

def test_get_all_students(student_service, mock_student):
    """Test retrieving all students."""
    with patch('src.repositories.student_repository.get_all_students', return_value=[mock_student]) as mock_get_all:
        result = student_service.get_all_students()
        mock_get_all.assert_called_once()
        assert len(result) == 1
        assert result[0] == mock_student