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
    student_email = "john.doe@example.com"
    
    # Act
    created_student = student_service.create_student(student_name, student_email)
    
    # Assert
    assert created_student.name == student_name
    assert created_student.email == student_email

def test_create_student_without_email(setup_database):
    # Arrange
    student_service = StudentService(setup_database)
    student_name = "Jane Doe"
    
    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        student_service.create_student(student_name, None)
    assert "Email is required" in str(excinfo.value)

def test_create_student_with_invalid_email(setup_database):
    # Arrange
    student_service = StudentService(setup_database)
    student_name = "Invalid Email Student"
    
    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        student_service.create_student(student_name, "invalid-email")
    assert "Invalid email format" in str(excinfo.value)

def test_retrieve_students(setup_database):
    # Arrange
    student_service = StudentService(setup_database)
    student_service.create_student("John Doe", "john.doe@example.com")
    student_service.create_student("Jane Doe", "jane.doe@example.com")
    
    # Act
    students = student_service.get_all_students()
    
    # Assert
    assert len(students) == 2
    assert students[0].email == "john.doe@example.com"
    assert students[1].email == "jane.doe@example.com"
```