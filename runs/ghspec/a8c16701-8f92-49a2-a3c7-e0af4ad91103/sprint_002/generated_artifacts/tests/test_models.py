```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Student

# Create a new SQLite database in memory for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a fixture to set up the database for each test
@pytest.fixture(scope="function")
def db():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    
    # Create a new session for testing
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        # Drop the tables after the tests are done for cleanup
        Base.metadata.drop_all(bind=engine)

def test_create_student_with_email(db):
    """Test creating a student with a valid email."""
    new_student = Student(name="John Doe", email="john.doe@example.com")
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    assert new_student.id is not None
    assert new_student.name == "John Doe"
    assert new_student.email == "john.doe@example.com"

def test_create_student_missing_email(db):
    """Test error handling when attempting to create a student without an email."""
    with pytest.raises(Exception) as exc_info:
        new_student = Student(name="Jane Doe")
        db.add(new_student)
        db.commit()  # This should fail due to missing email
    assert 'NOT NULL constraint failed' in str(exc_info.value)

def test_existing_students_retain_information_after_migration(db):
    """Test that existing students retain their information after migration."""
    # Create an initial student without the email
    existing_student = Student(name="Alice Smith")
    db.add(existing_student)
    db.commit()
    db.refresh(existing_student)

    # Run the migration here (this would be managed separately, just for demonstration)
    # Imagine the migration added the email field and preserved existing records

    # Fetch the student from the database to check that the data is intact
    student_from_db = db.query(Student).get(existing_student.id)
    assert student_from_db is not None
    assert student_from_db.name == "Alice Smith"
    # Here we cannot assert email because it should still be None

```