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
    
    assert student.id is not None, "Student ID should be set after creation"
    assert student.name == student_data['name'], "Student name should match input"
    assert student.email == student_data['email'], "Student email should match input"
    assert student.age == student_data['age'], "Student age should match input"

def test_get_student(student_repository):
    """Test retrieving an existing student by ID."""
    student_data = {
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com',
        'age': 22,
    }
    created_student = student_repository.create(student_data)
    
    retrieved_student = student_repository.get(created_student.id)
    
    assert retrieved_student is not None, "Should retrieve a student"
    assert retrieved_student.id == created_student.id, "Retrieved student ID should match created student's ID"
    assert retrieved_student.name == created_student.name, "Retrieved student name should match created student's name"

def test_get_student_not_found(student_repository):
    """Test retrieving a student that doesn't exist."""
    unknown_student_id = 9999  # Assuming this ID does not exist
    retrieved_student = student_repository.get(unknown_student_id)
    
    assert retrieved_student is None, "Should not find a student with unknown ID"

def test_create_student_with_invalid_email(student_repository):
    """Test creating a student with an invalid email format."""
    student_data = {
        'name': 'Invalid Email Student',
        'email': 'invalid-email-format',
        'age': 20,
    }
    with pytest.raises(ValueError, match="Invalid email format"):
        student_repository.create(student_data)

def test_update_student(student_repository):
    """Test updating an existing student's details."""
    student_data = {
        'name': 'Alice Smith',
        'email': 'alice.smith@example.com',
        'age': 19,
    }
    created_student = student_repository.create(student_data)
    
    updated_data = {
        'name': 'Alice Johnson',
        'email': 'alice.johnson@example.com',
        'age': 20,
    }
    
    updated_student = student_repository.update(created_student.id, updated_data)
    
    assert updated_student.name == updated_data['name'], "Student name should be updated"
    assert updated_student.email == updated_data['email'], "Student email should be updated"
    assert updated_student.age == updated_data['age'], "Student age should be updated"