```python
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

def test_create_student_with_email(db_session):
    """Test creating a student with a valid name and email."""
    new_student = Student(name="John Doe", email="john.doe@example.com")
    db_session.add(new_student)
    db_session.commit()
    
    # Validate that the student was created correctly
    created_student = db_session.query(Student).filter_by(email="john.doe@example.com").first()
    assert created_student is not None
    assert created_student.name == "John Doe"
    assert created_student.email == "john.doe@example.com"

def test_retrieve_student_email(db_session):
    """Test retrieving a student's information including email."""
    new_student = Student(name="Jane Doe", email="jane.doe@example.com")
    db_session.add(new_student)
    db_session.commit()

    retrieved_student = db_session.query(Student).filter_by(id=new_student.id).first()
    assert retrieved_student is not None
    assert retrieved_student.email == "jane.doe@example.com"

def test_create_student_without_email(db_session):
    """Test handling the case when a student is created without an email."""
    new_student = Student(name="John Smith")
    db_session.add(new_student)

    with pytest.raises(IntegrityError):
        db_session.commit()  # Expecting an IntegrityError due to missing email
        db_session.rollback()

def test_create_student_with_invalid_email_format(db_session):
    """Test handling the case for an invalid email format."""
    new_student = Student(name="Invalid Email", email="invalidemail")
    db_session.add(new_student)

    with pytest.raises(IntegrityError):
        db_session.commit()  # Expecting an IntegrityError due to invalid email format
        db_session.rollback()
```