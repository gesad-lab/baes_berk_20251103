import pytest
from src.models.student import Student
from src.services.student_service import StudentService
from src.schemas.student_schemas import CreateStudentSchema
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def student_service():
    # Assuming there is a way to initialize the service with a test database session
    service = StudentService()
    return service

def test_create_student_with_email(student_service):
    """Test creating a student with an email address."""
    student_data = CreateStudentSchema(name="John Doe", email="john.doe@example.com")
    student = student_service.create_student(student_data)

    assert student.name == student_data.name
    assert student.email == student_data.email

def test_create_student_with_invalid_email(student_service):
    """Test creating a student with an invalid email format raises an exception."""
    student_data = CreateStudentSchema(name="Jane Doe", email="invalid-email")

    with pytest.raises(IntegrityError):
        student_service.create_student(student_data)

def test_update_student_email(student_service):
    """Test updating a student's email address."""
    student_data = CreateStudentSchema(name="John Smith", email="john.smith@example.com")
    student = student_service.create_student(student_data)

    updated_email_data = CreateStudentSchema(name="John Smith", email="john.newemail@example.com")
    updated_student = student_service.update_student_email(student.id, updated_email_data.email)

    assert updated_student.email == updated_email_data.email

def test_retrieve_student_with_email(student_service):
    """Test retrieving a student and verify the email is included."""
    student_data = CreateStudentSchema(name="Alice Brown", email="alice.brown@example.com")
    student = student_service.create_student(student_data)

    retrieved_student = student_service.get_student_by_id(student.id)

    assert retrieved_student.name == student_data.name
    assert retrieved_student.email == student_data.email

def test_delete_student(student_service):
    """Test deleting a student."""
    student_data = CreateStudentSchema(name="Tom White", email="tom.white@example.com")
    student = student_service.create_student(student_data)

    delete_message = student_service.delete_student(student.id)

    assert delete_message == {"message": "Student deleted successfully"}
    assert student_service.get_student_by_id(student.id) is None  # Assuming the service returns None if not found