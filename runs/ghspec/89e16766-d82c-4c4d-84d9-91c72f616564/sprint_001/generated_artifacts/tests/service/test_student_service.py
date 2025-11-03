import pytest
from src.services.student_service import StudentService
from src.models.student import Student
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def setup_database(db_session):
    """Setup a fresh database session for each test."""
    yield db_session  # This provides the setup, and the teardown happens after each test

def test_create_student_with_valid_data(setup_database):
    """Test that a student record can be created successfully with valid data."""
    student_service = StudentService()
    student_data = {"name": "John Doe", "email": "john.doe@example.com"}

    student = student_service.create_student(student_data)
    
    # Check if the student was created with the correct attributes
    assert student.name == "John Doe"
    assert student.email == "john.doe@example.com"

def test_create_student_with_invalid_email(setup_database):
    """Test that an error is raised when an invalid email is provided."""
    student_service = StudentService()
    student_data = {"name": "Jane Doe", "email": "invalid_email"}

    with pytest.raises(ValueError) as exc_info:
        student_service.create_student(student_data)

    assert str(exc_info.value) == "E001: Invalid email format"

def test_create_student_without_name(setup_database):
    """Test that an error is raised when no name is provided."""
    student_service = StudentService()
    student_data = {"email": "john.doe@example.com"}

    with pytest.raises(ValueError) as exc_info:
        student_service.create_student(student_data)

    assert str(exc_info.value) == "E002: Name is required"

def test_retrieve_student_by_id(setup_database):
    """Test that a student record can be retrieved by ID."""
    student_service = StudentService()
    student_data = {"name": "Mark Smith", "email": "mark.smith@example.com"}
    student = student_service.create_student(student_data)
    
    retrieved_student = student_service.get_student_by_id(student.id)
    
    assert retrieved_student is not None
    assert retrieved_student.name == "Mark Smith"
    assert retrieved_student.email == "mark.smith@example.com"

def test_retrieve_non_existent_student(setup_database):
    """Test that trying to retrieve a non-existent student raises an error."""
    student_service = StudentService()
    
    with pytest.raises(ValueError) as exc_info:
        student_service.get_student_by_id(999)  # Assume 999 does not exist

    assert str(exc_info.value) == "E003: Student not found"