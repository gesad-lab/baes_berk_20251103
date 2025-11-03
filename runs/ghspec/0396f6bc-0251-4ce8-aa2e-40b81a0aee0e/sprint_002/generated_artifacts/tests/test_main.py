import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student  # Assuming your models are here and Student is imported
from your_app import create_student  # Adjust the import based on your application structure

# Setup for SQLite in-memory database for testing
@pytest.fixture(scope='module')
def test_database():
    # Create a new SQLite database (in-memory)
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # Create the tables

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session  # This will be the session for the scope of the test

    session.close()  # Close the session after tests are complete


def test_create_student_with_valid_data(test_database):
    """Test successful creation of a student with valid data."""
    student_data = {'name': 'John Doe', 'email': 'john@example.com'}

    student = create_student(test_database, **student_data)
    
    # Ensure that the student is created and saved in the database
    assert student.id is not None
    assert student.name == student_data['name']
    assert student.email == student_data['email']
    
    # Verify that the student has been added to the session
    saved_student = test_database.query(Student).filter_by(email=student_data['email']).first()
    assert saved_student is not None
    assert saved_student.name == student_data['name']


def test_create_student_with_duplicate_email(test_database):
    """Test creating a student with a duplicate email raises an error."""
    student_data = {'name': 'Jane Doe', 'email': 'jane@example.com'}
    create_student(test_database, **student_data)  # First creation should succeed

    # Attempting to create another student with the same email should fail
    duplicate_student_data = {'name': 'Another Jane', 'email': 'jane@example.com'}
    
    with pytest.raises(Exception) as exc_info:  # Adjust according to the specific exception raised
        create_student(test_database, **duplicate_student_data)
        
    assert 'duplicate key value violates unique constraint' in str(exc_info.value)


def test_create_student_with_invalid_email_format(test_database):
    """Test creating a student with an invalid email format raises an error."""
    invalid_student_data = {'name': 'Invalid Email', 'email': 'invalid-email-format'}
    
    with pytest.raises(Exception) as exc_info:  # Change based on your validation exceptions
        create_student(test_database, **invalid_student_data)

    assert 'not a valid email address' in str(exc_info.value)  # Adjust the message accordingly


def test_create_student_with_empty_email(test_database):
    """Test creating a student with no email raises an error."""
    invalid_student_data = {'name': 'No Email', 'email': ''}
    
    with pytest.raises(Exception) as exc_info:
        create_student(test_database, **invalid_student_data)

    assert 'Email field cannot be empty' in str(exc_info.value)  # Adjust the message accordingly