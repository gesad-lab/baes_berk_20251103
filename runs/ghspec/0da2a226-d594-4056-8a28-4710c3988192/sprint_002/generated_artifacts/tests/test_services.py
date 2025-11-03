```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from student_service import create_student, get_student, update_student, delete_student

# Set up the database in memory for tests
@pytest.fixture(scope='module')
def test_db():
    # Create an in-memory SQLite database
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # Create all tables
    connection = engine.connect()  # Connect to the database
    transaction = connection.begin()  # Begin a transaction
    
    # Create a session maker
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session  # Provide the session to the tests
    
    transaction.rollback()  # Rollback transaction after tests
    connection.close()  # Close the connection

@pytest.fixture
def sample_student(test_db):
    # Create a sample student for tests
    student = Student(name="John Doe", email="john@example.com")
    test_db.add(student)
    test_db.commit()
    return student

def test_create_student(test_db):
    # Test creating a student
    student = create_student("Jane Doe", "jane@example.com", test_db)
    assert student.id is not None
    assert student.name == "Jane Doe"
    assert student.email == "jane@example.com"

def test_get_student(test_db, sample_student):
    # Test retrieving a student
    student = get_student(sample_student.id, test_db)
    assert student.name == sample_student.name
    assert student.email == sample_student.email

def test_update_student(test_db, sample_student):
    # Test updating a student's email
    updated_student = update_student(sample_student.id, "john.doe@example.com", test_db)
    assert updated_student.email == "john.doe@example.com"

def test_delete_student(test_db, sample_student):
    # Test deleting a student
    delete_student(sample_student.id, test_db)
    student = get_student(sample_student.id, test_db)
    assert student is None  # Ensure the student no longer exists
```