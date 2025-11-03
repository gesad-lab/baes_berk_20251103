```python
import pytest
from src.services.teacher_service import TeacherService
from src.repositories.teacher_repository import TeacherRepository
from src.models.teacher import Teacher

@pytest.fixture
def teacher_service():
    # Mock the TeacherRepository for testing
    repository = TeacherRepository()
    service = TeacherService(repository)
    return service

def test_create_teacher_without_name(teacher_service):
    """Test creating a teacher without a name returns a validation error."""
    invalid_teacher_data = {"email": "teacher@example.com"}
    
    with pytest.raises(ValueError) as exc_info:
        teacher_service.create_teacher(invalid_teacher_data)
    
    # Verify the appropriate error message is raised
    assert str(exc_info.value) == "Validation Error: Name is required."

def test_create_teacher_without_email(teacher_service):
    """Test creating a teacher without an email returns a validation error."""
    invalid_teacher_data = {"name": "John Doe"}
    
    with pytest.raises(ValueError) as exc_info:
        teacher_service.create_teacher(invalid_teacher_data)
    
    # Verify the appropriate error message is raised
    assert str(exc_info.value) == "Validation Error: Email is required."

def test_create_teacher_without_name_and_email(teacher_service):
    """Test creating a teacher without name and email returns multiple validation errors."""
    invalid_teacher_data = {}
    
    with pytest.raises(ValueError) as exc_info:
        teacher_service.create_teacher(invalid_teacher_data)

    # Verify the appropriate error message is raised for both fields
    assert str(exc_info.value) == "Validation Error: Name is required. Email is required."
```