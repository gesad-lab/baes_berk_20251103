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

def test_create_student_with_valid_data(setup_database):
    # Arrange
    student_service = StudentService(setup_database)
    valid_student_name = "John Doe"
    valid_student_email = "john.doe@example.com"

    # Act
    created_student = student_service.create_student(name=valid_student_name, email=valid_student_email)

    # Assert
    assert created_student.name == valid_student_name
    assert created_student.email == valid_student_email

def test_create_student_without_name(setup_database):
    # Arrange
    student_service = StudentService(setup_database)
    invalid_student_name = ""  # Empty name
    valid_student_email = "john.doe@example.com"

    # Act & Assert
    with pytest.raises(ValueError, match="name is required"):
        student_service.create_student(name=invalid_student_name, email=valid_student_email)

def test_create_student_with_invalid_email(setup_database):
    # Arrange
    student_service = StudentService(setup_database)
    valid_student_name = "John Doe"
    invalid_student_email = "john.doe"  # Invalid email format

    # Act & Assert
    with pytest.raises(ValueError, match="Invalid email format"):
        student_service.create_student(name=valid_student_name, email=invalid_student_email)

def test_get_all_students(setup_database):
    # Arrange
    student_service = StudentService(setup_database)
    student_service.create_student(name="Alice Smith", email="alice.smith@example.com")
    student_service.create_student(name="Bob Johnson", email="bob.johnson@example.com")

    # Act
    all_students = student_service.get_all_students()

    # Assert
    assert len(all_students) == 2
    assert all_students[0].name == "Alice Smith"
    assert all_students[1].name == "Bob Johnson"
    assert all_students[0].email == "alice.smith@example.com"
    assert all_students[1].email == "bob.johnson@example.com"
```