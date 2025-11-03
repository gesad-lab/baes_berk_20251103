import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.student import Student
from src.database import Base


@pytest.fixture(scope='module')
def test_db():
    # Set up the SQLite in-memory database for testing
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # Create the database schema
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session  # Provide the test session to the tests

    session.close()  # Clean up after tests
    Base.metadata.drop_all(engine)  # Drop the database schema


def test_create_student(test_db):
    """Test creating a new student."""
    student = Student(name='John Doe')
    test_db.add(student)
    test_db.commit()
    
    assert student.id is not None  # Ensure the student has been assigned an ID
    retrieved_student = test_db.query(Student).filter_by(id=student.id).first()
    assert retrieved_student.name == 'John Doe'  # Check if the retrieved student has the correct name


def test_create_student_without_name(test_db):
    """Test creating a student without a name should raise an error."""
    student = Student(name=None)
    
    test_db.add(student)
    
    with pytest.raises(Exception):  # Replace Exception with the specific exception type when raised
        test_db.commit()  # Attempt to commit without a valid name


def test_retrieve_student(test_db):
    """Test retrieving a student by ID."""
    student = Student(name='Jane Doe')
    test_db.add(student)
    test_db.commit()

    retrieved_student = test_db.query(Student).filter_by(id=student.id).first()
    
    assert retrieved_student is not None  # Ensure the student is found
    assert retrieved_student.name == 'Jane Doe'  # Check the name matches


def test_retrieve_nonexistent_student(test_db):
    """Test retrieving a student that does not exist returns None."""
    retrieved_student = test_db.query(Student).filter_by(id=999).first()  # Assume 999 does not exist
    assert retrieved_student is None  # Ensure the result is None


def test_create_multiple_students(test_db):
    """Test creating multiple students and verifying their count."""
    students = [Student(name=f'Student {i}') for i in range(10)]
    
    for student in students:
        test_db.add(student)
    test_db.commit()
    
    all_students = test_db.query(Student).all()
    assert len(all_students) == 10  # Verify we have 10 students in the database
    assert all(student.name.startswith('Student') for student in all_students)  # Ensure names start as expected