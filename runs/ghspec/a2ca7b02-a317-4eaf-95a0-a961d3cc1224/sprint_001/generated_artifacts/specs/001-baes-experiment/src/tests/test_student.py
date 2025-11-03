```python
import pytest
from services.student_service import StudentService
from db.database import Database
from models.student import Student

@pytest.fixture
def setup_database():
    # Setup an in-memory SQLite database for testing
    db = Database('sqlite:///:memory:')
    db.create_schema()
    yield db
    # Cleanup after tests
    db.close()

def test_create_student(setup_database):
    # Arrange
    student_service = StudentService(setup_database)
    student_name = "John Doe"
    
    # Act
    created_student = student_service.create_student(student_name)

    # Assert
    assert created_student.name == student_name
    assert isinstance(created_student, Student)

def test_create_student_with_empty_name(setup_database):
    # Arrange
    student_service = StudentService(setup_database)
    
    # Act & Assert
    with pytest.raises(ValueError):
        student_service.create_student("")

def test_create_student_with_duplicate_name(setup_database):
    # Arrange
    student_service = StudentService(setup_database)
    student_name = "Jane Doe"
    student_service.create_student(student_name)  # Create initial student

    # Act & Assert
    with pytest.raises(ValueError):
        student_service.create_student(student_name)  # Attempt to create duplicate student
```