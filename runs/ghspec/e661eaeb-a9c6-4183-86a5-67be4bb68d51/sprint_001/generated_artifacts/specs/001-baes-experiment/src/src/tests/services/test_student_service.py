import pytest
from src.services.student_service import StudentService
from src.models.student import Student
from src.database.database import SessionLocal
from fastapi import HTTPException

# Initialize the in-memory SQLite database for testing
@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.close()

@pytest.fixture
def student_service(db_session):
    return StudentService(db_session)

def test_create_student(student_service):
    """Test creating a new student."""
    student_data = {"name": "John Doe"}
    created_student = student_service.create_student(student_data)
    
    assert created_student.name == student_data["name"]
    assert created_student.id is not None

def test_get_student(student_service):
    """Test retrieving a student."""
    student_data = {"name": "Jane Doe"}
    created_student = student_service.create_student(student_data)
    
    retrieved_student = student_service.get_student(created_student.id)
    
    assert retrieved_student.name == created_student.name
    assert retrieved_student.id == created_student.id

def test_update_student(student_service):
    """Test updating a student's name."""
    student_data = {"name": "John Smith"}
    created_student = student_service.create_student(student_data)
    
    updated_data = {"name": "John Doe Jr."}
    updated_student = student_service.update_student(created_student.id, updated_data)
    
    assert updated_student.name == updated_data["name"]
    assert updated_student.id == created_student.id

def test_delete_student(student_service):
    """Test deleting a student."""
    student_data = {"name": "Delete Me"}
    created_student = student_service.create_student(student_data)
    
    # Ensure the student exists before deletion
    student_service.get_student(created_student.id)

    # Delete the student
    student_service.delete_student(created_student.id)
    
    # Verify the student is deleted
    with pytest.raises(HTTPException) as exc_info:
        student_service.get_student(created_student.id)
    
    assert exc_info.value.status_code == 404  # Not Found
    assert exc_info.value.detail == "Student not found"  # Replace with actual error message

This test file defines the unit tests for the student service logic, ensuring that the core functionality (create, retrieve, update, and delete students) behaves as expected. It uses pytest for the testing framework and assumes that the service layer methods are properly defined in `student_service.py`.