```python
import pytest
from src.services import StudentService
from src.models import Student


@pytest.fixture
def setup_student_service():
    """Fixture to set up the StudentService for testing."""
    service = StudentService()
    return service


def test_create_student_success(setup_student_service):
    """Test case for successfully creating a student."""
    student_data = {
        "name": "John Doe",
        "age": 21,
        "email": "john.doe@example.com"
    }
    
    created_student = setup_student_service.create_student(student_data)
    
    assert created_student.name == student_data["name"]
    assert created_student.age == student_data["age"]
    assert created_student.email == student_data["email"]


def test_create_student_with_invalid_data(setup_student_service):
    """Test case for creating a student with invalid data."""
    student_data = {
        "name": "",
        "age": 21,
        "email": "john.doe@example.com"
    }
    
    # Check for ValueError when trying to create a student with invalid name
    with pytest.raises(ValueError) as excinfo:
        setup_student_service.create_student(student_data)
    
    assert "Name cannot be empty" in str(excinfo.value)


def test_get_student_success(setup_student_service):
    """Test case for fetching an existing student."""
    student_data = {
        "name": "Jane Doe",
        "age": 22,
        "email": "jane.doe@example.com"
    }
    
    created_student = setup_student_service.create_student(student_data)
    fetched_student = setup_student_service.get_student(created_student.id)
    
    assert fetched_student.id == created_student.id
    assert fetched_student.name == created_student.name
    assert fetched_student.age == created_student.age
    assert fetched_student.email == created_student.email


def test_get_student_not_found(setup_student_service):
    """Test case for fetching a student that does not exist."""
    # Attempt to fetch a student with an ID that doesn't exist
    with pytest.raises(ValueError) as excinfo:
        setup_student_service.get_student(999)  # Assuming 999 does not exist
    
    assert "Student not found" in str(excinfo.value)
```