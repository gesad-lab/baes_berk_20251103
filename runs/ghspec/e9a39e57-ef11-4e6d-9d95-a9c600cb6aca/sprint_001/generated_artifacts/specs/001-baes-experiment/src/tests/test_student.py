import pytest
from src.models import Student
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.database import get_db


@pytest.fixture
def db_session():
    """Create a new database session for a test."""
    session = get_db()  # Assuming get_db creates a new session
    yield session
    session.close()


def test_create_student(db_session):
    """Test creating a student with valid data."""
    new_student = Student(name="John Doe")
    db_session.add(new_student)
    db_session.commit()
    db_session.refresh(new_student)

    assert new_student.id is not None
    assert new_student.name == "John Doe"


def test_create_student_without_name(db_session):
    """Test creating a student without a name raises an error."""
    with pytest.raises(IntegrityError):
        new_student = Student(name=None)  # Name is required
        db_session.add(new_student)
        db_session.commit()


def test_retrieve_student(db_session):
    """Test retrieving a student by ID."""
    student = Student(name="Jane Doe")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    retrieved_student = db_session.query(Student).filter_by(id=student.id).first()
    
    assert retrieved_student is not None
    assert retrieved_student.name == "Jane Doe"


def test_retrieve_nonexistent_student(db_session):
    """Test retrieving a student that does not exist returns None."""
    non_existent_student = db_session.query(Student).filter_by(id=999).first()
    assert non_existent_student is None