import pytest
from src.services.student_service import create_student, list_students
from src.models import Student  # Assuming you have a Student model defined elsewhere
from sqlalchemy.orm import Session

# Mocking the database session
class MockSession:
    def __init__(self):
        self.students = []
    
    def add(self, student):
        self.students.append(student)
    
    def commit(self):
        pass  # Simulate commit

    def query(self, model):
        return self

    def all(self):
        return self.students
    
    def filter(self, *args, **kwargs):
        # Basic filtering logic for testing
        return self

@pytest.fixture
def db_session():
    """Fixture for mocking the database session."""
    return MockSession()

def test_create_student(db_session):
    """Test creating a new student successfully."""
    name = "John Doe"
    student = create_student(name, db_session)
    
    assert isinstance(student, Student)
    assert student.name == name
    assert len(db_session.students) == 1

def test_list_students(db_session):
    """Test listing students."""
    db_session.add(Student(name="John Doe"))
    db_session.add(Student(name="Jane Smith"))
    db_session.commit()

    students = list_students(db_session)
    
    assert isinstance(students, list)
    assert len(students) == 2
    assert students[0].name == "John Doe"
    assert students[1].name == "Jane Smith"

def test_create_student_missing_name(db_session):
    """Test error handling when creating a student without a name."""
    with pytest.raises(ValueError) as excinfo:
        create_student("", db_session)
    
    assert str(excinfo.value) == "Name field is required"  # Adjust to your actual error handling message

def test_create_student_invalid_name(db_session):
    """Test error handling when creating a student with an invalid name."""
    with pytest.raises(ValueError) as excinfo:
        create_student(None, db_session)
    
    assert str(excinfo.value) == "Name field is required"  # Adjust to your actual error handling message

# Add more tests as needed for other scenarios and edge cases