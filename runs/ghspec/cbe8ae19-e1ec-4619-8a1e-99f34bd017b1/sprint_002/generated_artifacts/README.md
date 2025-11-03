# Updated File Content for: tests/test_api.py

```python
import pytest
from student_repository import StudentRepository
from models import Student, db

@pytest.fixture
def setup_database():
    """Setup a test database before each test."""
    db.create_all()  # Create the database tables
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Drop all tables after tests

@pytest.fixture
def student_repository(setup_database):
    """Fixture for the StudentRepository."""
    return StudentRepository()

def test_create_student_with_email(student_repository):
    """Test creating a student with a valid email."""
    student_data = {'name': 'Jane Doe', 'email': 'jane.doe@example.com'}
    response = student_repository.add_student(student_data)
    assert response is not None
    assert response.name == 'Jane Doe'
    assert response.email == 'jane.doe@example.com'

def test_retrieve_student_by_id(student_repository):
    """Test retrieving a student by ID."""
    student_data = {'name': 'Jane Doe', 'email': 'jane.doe@example.com'}
    student = student_repository.add_student(student_data)
    response = student_repository.get_student_by_id(student.id)
    assert response is not None
    assert response.id == student.id
    assert response.email == 'jane.doe@example.com'

def test_list_all_students(student_repository):
    """Test listing all students."""
    student_data1 = {'name': 'Alice Smith', 'email': 'alice@example.com'}
    student_data2 = {'name': 'Bob Johnson', 'email': 'bob@example.com'}
    student_repository.add_student(student_data1)
    student_repository.add_student(student_data2)

    response = student_repository.get_all_students()
    assert len(response) == 2
    assert response[0].email == 'alice@example.com'
    assert response[1].email == 'bob@example.com'
```