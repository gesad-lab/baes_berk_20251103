```python
import pytest
from src.database import get_db, init_db
from src.models import Student, Course, StudentCourse
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test

def test_create_student_course_valid(db):
    """Test creating a new student-course relationship with valid data."""
    student = Student(name="John Doe")
    course = Course(name="Mathematics", level="Beginner")
    
    db.session.add(student)
    db.session.add(course)
    db.session.commit()

    student_course = StudentCourse(student_id=student.id, course_id=course.id)
    db.session.add(student_course)
    db.session.commit()

    # Verify the student-course relationship was created
    assert student_course.student_id == student.id
    assert student_course.course_id == course.id

def test_create_student_course_invalid_student(db):
    """Test creating a student-course relationship with an invalid student ID."""
    course = Course(name="Mathematics", level="Beginner")
    
    db.session.add(course)
    db.session.commit()
    
    with pytest.raises(IntegrityError):
        student_course = StudentCourse(student_id=999, course_id=course.id)  # Invalid student ID
        db.session.add(student_course)
        db.session.commit()

def test_create_student_course_invalid_course(db):
    """Test creating a student-course relationship with an invalid course ID."""
    student = Student(name="John Doe")
    
    db.session.add(student)
    db.session.commit()
    
    with pytest.raises(IntegrityError):
        student_course = StudentCourse(student_id=student.id, course_id=999)  # Invalid course ID
        db.session.add(student_course)
        db.session.commit()
```