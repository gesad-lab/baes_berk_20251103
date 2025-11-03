import pytest
from src.models.student import Student
from src.repositories.student_repository import StudentRepository

@pytest.fixture
def student_repository():
    """Fixture for initializing the StudentRepository for tests."""
    return StudentRepository()

def test_create_student(student_repository):
    """Test creating a new student."""
    student_data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'age': 20,
    }
    student = student_repository.create(student_data)
    assert student.name == student_data['name']
    assert student.email == student_data['email']

def test_create_student_with_email(student_repository):
    """Test creating a new student with email."""
    student_data = {
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    }
    student = student_repository.create(student_data)
    assert student.email == 'jane.doe@example.com'
    assert student.name == 'Jane Doe'

def test_create_student_without_email(student_repository):
    """Test creating a new student without email."""
    student_data = {
        'name': 'Mark Smith',
        'age': 22,
    }
    student = student_repository.create(student_data)
    assert student.name == 'Mark Smith'
    assert student.email is None  # Assuming the email is nullable

def test_create_student_with_invalid_email(student_repository):
    """Test creating a student with an invalid email format."""
    student_data = {
        'name': 'Invalid Email Student',
        'email': 'invalid-email'
    }
    with pytest.raises(ValueError) as exc_info:
        student_repository.create(student_data)
    
    assert str(exc_info.value) == 'Invalid email format'  # Assuming this is the raised error message

def test_retrieve_student_with_email(student_repository):
    """Test retrieving a student by ID includes email."""
    student_data = {
        'name': 'Alice Cooper',
        'email': 'alice.cooper@example.com'
    }
    student = student_repository.create(student_data)
    retrieved_student = student_repository.get_by_id(student.id)
    
    assert retrieved_student.id == student.id
    assert retrieved_student.name == student.name
    assert retrieved_student.email == student.email