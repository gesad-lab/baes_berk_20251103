```python
import pytest
from src.models import Student  # Assuming this is the correct path for the Student model
from src.repositories import StudentRepository  # Assuming a repository exists for data operations
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def student_repository():
    """Fixture for creating a student repository for testing."""
    return StudentRepository()

@pytest.fixture
def new_student():
    """Fixture for a new student with valid attributes."""
    return Student(name="John Doe", email="john.doe@example.com")

def test_create_student_with_email(student_repository, new_student):
    """Test creating a new student with an email."""
    student_repository.create(new_student)
    retrieved_student = student_repository.get(student_repository.last_inserted_id)  # Assuming the repo provides last inserted ID
    assert retrieved_student is not None
    assert retrieved_student.name == "John Doe"
    assert retrieved_student.email == "john.doe@example.com"

def test_create_student_without_email(student_repository):
    """Test creation fails without an email."""
    with pytest.raises(IntegrityError):  # Assuming IntegrityError is raised for missing required fields
        student_repository.create(Student(name="Jane Doe"))

def test_update_student_email(student_repository, new_student):
    """Test updating a student's email."""
    student_repository.create(new_student)
    updated_email = "john.new@example.com"
    new_student.email = updated_email
    student_repository.update(new_student)  # Assuming the repository has an update method
    retrieved_student = student_repository.get(student_repository.last_inserted_id)
    assert retrieved_student.email == updated_email

def test_retrieve_student_details(student_repository, new_student):
    """Test retrieving a student's details including their email."""
    student_repository.create(new_student)
    retrieved_student = student_repository.get(student_repository.last_inserted_id)
    assert retrieved_student is not None
    assert retrieved_student.name == "John Doe"
    assert retrieved_student.email == "john.doe@example.com"
```