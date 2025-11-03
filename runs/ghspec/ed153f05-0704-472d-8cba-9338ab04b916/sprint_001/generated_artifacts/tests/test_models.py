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
    student = Student(name="John Doe")
    db.session.add(student)
    db.session.commit()
    
    # Verify the student was added
    retrieved_student = db.session.query(Student).filter_by(name="John Doe").first()
    assert retrieved_student is not None
    assert retrieved_student.name == "John Doe"

def test_student_invalid_creation(db):
    """Test creation of a student record with invalid data."""
    student = Student(name=None)  # Invalid student (name is required)
    db.session.add(student)

    with pytest.raises(Exception) as excinfo:
        db.session.commit()
    assert "NOT NULL constraint failed" in str(excinfo.value)

def test_student_retrieval(db):
    """Test retrieval of student records."""
    student = db.session.query(Student).filter_by(name="John Doe").first()
    assert student is not None

def test_student_deletion(db):
    """Test deletion of a student record."""
    student = db.session.query(Student).filter_by(name="John Doe").first()
    db.session.delete(student)
    db.session.commit()
    
    # Verify the student was deleted
    deleted_student = db.session.query(Student).filter_by(name="John Doe").first()
    assert deleted_student is None

def test_db_schema_migration(db):
    """Ensure that migrations are correctly applied."""
    # Assuming we have a function to verify the schema
    assert db.has_table('student')  # Check the database has the 'student' table
    # Add additional schema verification as needed
```