import pytest
from sqlalchemy.orm import Session
from src.models import Student
from src.services.student_service import create_student, get_student, update_student, delete_student
from src.database import get_db

@pytest.fixture
def test_db():
    # Set up a test database connection and session
    db = get_db()
    yield db
    db.rollback()  # Ensure rollback after tests to maintain isolation
    db.close()

def test_create_student(test_db: Session):
    # Test data for creating a student
    student_data = {"name": "John Doe", "email": "john.doe@example.com"}
    student = create_student(db=test_db, **student_data)
    assert student.name == student_data["name"]
    assert student.email == student_data["email"]

def test_create_student_empty_email(test_db: Session):
    # Attempt to create a student with an empty email field
    student_data = {"name": "Jane Doe", "email": ""}
    with pytest.raises(ValueError, match="Email field is required"):
        create_student(db=test_db, **student_data)

def test_get_all_students(test_db: Session):
    # Add sample students to the database
    create_student(db=test_db, name="Alice Smith", email="alice.smith@example.com")
    create_student(db=test_db, name="Bob Johnson", email="bob.johnson@example.com")
    
    students = get_student(db=test_db)
    assert len(students) == 2
    for student in students:
        assert student.email  # Ensure email field is included

def test_update_student_email(test_db: Session):
    # Create a student to update
    student_data = {"name": "Chris Evans", "email": "chris.evans@example.com"}
    student = create_student(db=test_db, **student_data)

    # Update the student's email
    updated_data = {"name": "Chris Evans", "email": "updated.chris@example.com"}
    updated_student = update_student(db=test_db, student_id=student.id, **updated_data)
    
    assert updated_student.email == updated_data["email"]

def test_delete_student_removes_email(test_db: Session):
    # Create a student to delete
    student_data = {"name": "Diana Prince", "email": "diana.prince@example.com"}
    student = create_student(db=test_db, **student_data)
    
    # Delete the student
    delete_student(db=test_db, student_id=student.id)
    
    # Verify student no longer exists
    with pytest.raises(ValueError, match="Student not found"):
        get_student(db=test_db, student_id=student.id)