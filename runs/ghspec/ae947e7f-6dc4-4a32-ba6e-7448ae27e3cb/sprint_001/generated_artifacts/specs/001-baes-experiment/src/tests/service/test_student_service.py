import pytest
from src.service.student_service import create_student, get_student_by_id
from src.model.student import Student
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from unittest.mock import MagicMock

@pytest.fixture
def db_session():
    # Create a new session for each test
    session = Session()
    yield session
    session.close()

def test_create_student_success(db_session):
    """Test creating a student with a valid name."""
    
    student_name = "John Doe"
    student = create_student(name=student_name, db_session=db_session)

    assert isinstance(student, Student)
    assert student.name == student_name

def test_create_student_no_name(db_session):
    """Test creating a student without a name raises an error."""
    
    with pytest.raises(ValueError) as excinfo:
        create_student(name="", db_session=db_session)

    assert str(excinfo.value) == "Name is required."

def test_get_student_by_id_success(db_session):
    """Test retrieving a student by valid ID."""
    
    student_name = "Jane Smith"
    student = create_student(name=student_name, db_session=db_session)

    fetched_student = get_student_by_id(student_id=student.id, db_session=db_session)

    assert isinstance(fetched_student, Student)
    assert fetched_student.name == student_name

def test_get_student_by_id_not_found(db_session):
    """Test retrieving a non-existent student raises an error."""
    
    with pytest.raises(ValueError) as excinfo:
        get_student_by_id(student_id=9999, db_session=db_session)

    assert str(excinfo.value) == "Student not found."
