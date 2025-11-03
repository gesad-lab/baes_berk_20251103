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

def test_save_student(student_repository):
    """Test saving a student to the database."""
    student = Student(name="John Doe", age=20)
    student_repository.save(student)

    # Query the database to check if the student was saved
    saved_student = Student.query.filter_by(name="John Doe").first()
    assert saved_student is not None
    assert saved_student.age == 20

def test_find_student_by_id(student_repository):
    """Test finding a student by ID."""
    student = Student(name="Jane Doe", age=22)
    db.session.add(student)
    db.session.commit()  # Commit to save student to the database

    found_student = student_repository.find_by_id(student.id)
    assert found_student is not None
    assert found_student.name == "Jane Doe"

def test_retrieve_all_students(student_repository):
    """Test retrieving all students from the database."""
    student1 = Student(name="Alice", age=19)
    student2 = Student(name="Bob", age=21)
    db.session.add(student1)
    db.session.add(student2)
    db.session.commit()  # Before retrieval, ensure students are saved

    students = student_repository.retrieve_all()
    assert len(students) == 2
    assert any(student.name == "Alice" for student in students)
    assert any(student.name == "Bob" for student in students)
```