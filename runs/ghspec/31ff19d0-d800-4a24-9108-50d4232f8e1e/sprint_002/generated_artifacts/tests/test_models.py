import pytest
from src.models import Student
from src.database import db


@pytest.fixture
def create_student():
    """Fixture to create a new student in the database for testing."""
    def _create_student(name, email):
        student = Student(name=name, email=email)
        db.session.add(student)
        db.session.commit()
        return student
    return _create_student


def test_add_student_with_email(create_student):
    """Test adding a new student with valid name and email."""
    student = create_student("John Doe", "john.doe@example.com")
    assert student.id is not None
    assert student.name == "John Doe"
    assert student.email == "john.doe@example.com"


def test_retrieve_all_students(create_student):
    """Test retrieving all students."""
    create_student("Alice Smith", "alice.smith@example.com")
    create_student("Bob Brown", "bob.brown@example.com")

    students = Student.query.all()
    assert len(students) == 2
    assert students[0].name == "Alice Smith"
    assert students[1].name == "Bob Brown"


def test_add_student_without_email():
    """Test adding a student without providing an email address."""
    student = Student(name="Charlie Green", email=None)
    
    with pytest.raises(Exception) as exc_info:
        db.session.add(student)
        db.session.commit()
    
    assert "not-null" in str(exc_info.value)  # Check error for not-null constraint


def test_add_student_with_duplicate_email(create_student):
    """Test adding a student with an email that already exists."""
    create_student("David White", "david.white@example.com")

    duplicate_student = Student(name="Eve Black", email="david.white@example.com")
    
    with pytest.raises(Exception) as exc_info:
        db.session.add(duplicate_student)
        db.session.commit()
    
    assert "unique constraint" in str(exc_info.value)  # Check error for unique constraint