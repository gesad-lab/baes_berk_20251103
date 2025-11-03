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

@pytest.fixture
def add_sample_students(student_repository):
    """Fixture to add sample students to the database."""
    student1 = Student(name='John Doe', email='john@example.com')
    student2 = Student(name='Jane Smith', email='jane@example.com')
    
    db.session.add(student1)
    db.session.add(student2)
    db.session.commit()

def test_get_all_students_includes_email(student_repository, add_sample_students):
    """Test that get_all_students includes email in the response."""
    
    # Act: Retrieve all students
    students = student_repository.get_all_students()

    # Assert: Check if the response includes emails
    assert len(students) == 2
    assert all(hasattr(student, 'email') for student in students)
    assert any(student.email == 'john@example.com' for student in students)
    assert any(student.email == 'jane@example.com' for student in students)

def test_get_all_students_empty(student_repository):
    """Test that get_all_students returns an empty list when no students are present."""
    
    # Act: Retrieve all students
    students = student_repository.get_all_students()

    # Assert: Verify that the response is an empty list
    assert students == []
```