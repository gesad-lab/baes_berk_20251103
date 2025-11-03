# /student_management_app/tests/test_models.py

import pytest
from src.models import Student
from src.database import db_session


@pytest.fixture(scope="module")
def new_student():
    """Fixture to create a new student for testing."""
    student = Student(name="John Doe")
    db_session.add(student)
    db_session.commit()
    yield student
    db_session.delete(student)
    db_session.commit()


def test_create_student(new_student):
    """Test the creation of a new student."""
    assert new_student.id is not None  # Ensure the student has an ID
    assert new_student.name == "John Doe"  # Ensure the name matches


def test_add_student_without_name():
    """Test that attempting to create a student without a name raises an error."""
    with pytest.raises(ValueError) as excinfo:
        student = Student(name=None)  # Name is required
        db_session.add(student)
        db_session.commit()
    
    assert "name is required" in str(excinfo.value)  # Check for the validation error


def test_retrieve_students():
    """Test retrieving all students."""
    # Given: Create a few students
    student1 = Student(name="Alice")
    student2 = Student(name="Bob")
    db_session.add(student1)
    db_session.add(student2)
    db_session.commit()

    # When: Retrieve all students
    students = db_session.query(Student).all()

    # Then: Ensure the list contains the students
    assert len(students) >= 2  # Ensure we have at least two students
    assert any(s.name == "Alice" for s in students)
    assert any(s.name == "Bob" for s in students)

    # Cleanup
    db_session.delete(student1)
    db_session.delete(student2)
    db_session.commit()