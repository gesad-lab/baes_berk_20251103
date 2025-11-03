```python
import pytest
from unittest.mock import patch, MagicMock
from src.services.teacher_service import create_teacher, get_teacher_by_id
from src.models import Teacher
from your_app import db  # Ensure to replace with the actual import path

@pytest.fixture
def mock_teacher():
    """Create a mock teacher data for testing."""
    return Teacher(id=1, name="John Doe", email="john@example.com")

def test_create_teacher_success():
    """Test successful teacher creation."""
    with patch('src.services.teacher_service.db.session.add') as mock_add, \
         patch('src.services.teacher_service.db.session.commit') as mock_commit:
        teacher_data = {"name": "John Doe", "email": "john@example.com"}
        
        result = create_teacher(teacher_data)
        
        assert result['message'] == "Teacher created successfully."
        mock_add.assert_called_once()
        mock_commit.assert_called_once()

def test_create_teacher_missing_name():
    """Test error when creating a teacher with missing name."""
    teacher_data = {"email": "john@example.com"}
    
    with pytest.raises(ValueError) as excinfo:
        create_teacher(teacher_data)
        
    assert str(excinfo.value) == "Name and email are required."

def test_create_teacher_missing_email():
    """Test error when creating a teacher with missing email."""
    teacher_data = {"name": "John Doe"}
    
    with pytest.raises(ValueError) as excinfo:
        create_teacher(teacher_data)

    assert str(excinfo.value) == "Name and email are required."

def test_get_teacher_by_id_success(mock_teacher):
    """Test retrieval of teacher by ID."""
    with patch('src.services.teacher_service.Teacher.query.get') as mock_get:
        mock_get.return_value = mock_teacher
        
        result = get_teacher_by_id(1)
        
        assert result.id == mock_teacher.id
        assert result.name == mock_teacher.name
        assert result.email == mock_teacher.email

def test_get_teacher_by_id_not_found():
    """Test retrieval of a teacher that does not exist."""
    with patch('src.services.teacher_service.Teacher.query.get') as mock_get:
        mock_get.return_value = None
        
        result = get_teacher_by_id(99)
        
        assert result is None
```