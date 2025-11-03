import pytest
from src.database import get_db, init_db
from src.models import Student
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test

def test_student_creation_with_email(db):
    """Test creating a new student record with email."""
    student = Student(name="John Doe", email="john@example.com")  # Include email
    db.session.add(student)
    db.session.commit()
    assert student.id is not None
    assert student.name == "John Doe"
    assert student.email == "john@example.com"

def test_student_creation_without_email(db):
    """Test creating a new student record without email raises an error."""
    student = Student(name="Jane Doe")  # Missing email field
    db.session.add(student)
    with pytest.raises(IntegrityError):  # Expect an integrity error
        db.session.commit()
    db.session.rollback()  # Rollback the session after the error

def test_student_creation_without_name(db):
    """Test creating a new student record without name raises an error."""
    student = Student(email="jane@example.com")  # Missing name field
    db.session.add(student)
    with pytest.raises(IntegrityError):  # Expect an integrity error
        db.session.commit()
    db.session.rollback()  # Rollback the session after the error

def test_student_retrieval(db):
    """Test retrieving a student by ID."""
    student = Student(name="John Doe", email="john@example.com")
    db.session.add(student)
    db.session.commit()
    
    retrieved_student = Student.query.get(student.id)  # Retrieve by ID
    assert retrieved_student is not None
    assert retrieved_student.name == "John Doe"
    assert retrieved_student.email == "john@example.com"

def test_retrieve_all_students(db):
    """Test retrieving all students."""
    student1 = Student(name="Alice", email="alice@example.com")
    student2 = Student(name="Bob", email="bob@example.com")
    db.session.add_all([student1, student2])
    db.session.commit()
    
    students = Student.query.all()  # Retrieve all students
    assert len(students) == 2
    assert students[0].email in ["alice@example.com", "bob@example.com"]
    assert students[1].email in ["alice@example.com", "bob@example.com"]