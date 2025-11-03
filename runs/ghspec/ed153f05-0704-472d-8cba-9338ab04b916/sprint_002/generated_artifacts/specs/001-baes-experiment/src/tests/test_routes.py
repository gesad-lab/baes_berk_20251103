```python
import pytest
from src.database import get_db, init_db
from src.models import Student

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test
    # Teardown (not needed for in-memory DB)

def test_student_creation(db):
    """Test creating a new student record."""
    student = Student(name="John Doe", email="john.doe@example.com")
    db.session.add(student)
    db.session.commit()
    
    # Verify the student was created correctly
    assert student.id is not None  # ID should be set upon committing
    assert student.name == "John Doe"
    assert student.email == "john.doe@example.com"

def test_student_email_validation(db):
    """Test the email attribute for validation."""
    student = Student(name="Jane Doe", email="jane.doe@example.com")
    db.session.add(student)
    db.session.commit()
    
    retrieved_student = db.session.query(Student).filter_by(name="Jane Doe").first()
    
    # Verify that the email is stored correctly
    assert retrieved_student.email == "jane.doe@example.com"

def test_student_email_required(db):
    """Test that creating a student without an email raises an error."""
    invalid_student = Student(name="Invalid Student")  # No email provided
    db.session.add(invalid_student)
    
    with pytest.raises(Exception) as exc_info:  # Adjust this to the specific exception type
        db.session.commit()

    assert "NOT NULL constraint failed" in str(exc_info.value)  # Check if the error message is as expected

def test_student_update_email(db):
    """Test updating a student's email."""
    student = Student(name="John Smith", email="john.smith@example.com")
    db.session.add(student)
    db.session.commit()
    
    # Update the email address
    student.email = "john.newsmith@example.com"
    db.session.commit()
    
    updated_student = db.session.query(Student).filter_by(name="John Smith").first()
    
    # Verify the email update was successful
    assert updated_student.email == "john.newsmith@example.com"

def test_student_deletion(db):
    """Test deleting a student record."""
    student = Student(name="Mark Twain", email="mark.twain@example.com")
    db.session.add(student)
    db.session.commit()
    
    # Delete the student
    db.session.delete(student)
    db.session.commit()
    
    deleted_student = db.session.query(Student).filter_by(name="Mark Twain").first()
    
    # Verify the student was deleted
    assert deleted_student is None
```