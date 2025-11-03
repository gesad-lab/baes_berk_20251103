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
    Base.metadata.create_all(engine)
    connection = engine.connect()
    transaction = connection.begin()
    
    yield connection  # This is where the testing will happen

    transaction.rollback()  # Roll back the transaction
    connection.close()

# Test creating a student
def test_create_student(test_db):
    name = "John Doe"
    student_id = create_student(name)
    student = get_student(student_id)
    
    assert student is not None
    assert student.name == name

# Test retrieving student information
def test_get_student(test_db):
    name = "Jane Doe"
    student_id = create_student(name)
    student = get_student(student_id)
    
    assert student is not None
    assert student.id == student_id
    assert student.name == name

# Test updating a student's name
def test_update_student(test_db):
    name = "Alice Johnson"
    student_id = create_student(name)
    new_name = "Alice Smith"
    
    update_student(student_id, new_name)
    updated_student = get_student(student_id)
    
    assert updated_student.name == new_name

# Test deleting a student
def test_delete_student(test_db):
    name = "Bob Brown"
    student_id = create_student(name)
    
    delete_student(student_id)
    deleted_student = get_student(student_id)

    assert deleted_student is None  # Student should not be retrievable now
```