```python
import pytest
from src.models import Student, Course, StudentCourses  # Importing the models to be tested
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Mock database setup for testing
DATABASE_URL = "sqlite:///:memory:"  # Use in-memory SQLite database for tests
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@pytest.fixture(scope='module')
def setup_database():
    """Set up the in-memory database and create the tables for testing."""
    # Create all tables
    from src.models import Base  # Assuming Base is the declarative base
    Base.metadata.create_all(engine)
    
    yield Session()  # Provide a session to tests
    
    # Teardown
    Base.metadata.drop_all(engine)

@pytest.fixture
def new_student(setup_database):
    """Fixture to create a new student."""
    session = setup_database
    student = Student(name="John Doe", email="john@example.com")
    session.add(student)
    session.commit()
    session.refresh(student)  # Refresh to get the student with the generated id
    return student

@pytest.fixture
def new_course(setup_database):
    """Fixture to create a new course."""
    session = setup_database
    course = Course(name="Introduction to Programming")
    session.add(course)
    session.commit()
    session.refresh(course)  # Refresh to get the course with the generated id
    return course

def test_student_creation(new_student):
    """Test that a student is created successfully."""
    assert new_student.name == "John Doe"
    assert new_student.email == "john@example.com"

def test_course_creation(new_course):
    """Test that a course is created successfully."""
    assert new_course.name == "Introduction to Programming"

def test_student_courses_association(setup_database, new_student, new_course):
    """Test that student can be associated with a course."""
    session = setup_database
    association = StudentCourses(student_id=new_student.id, course_id=new_course.id)
    session.add(association)
    session.commit()
    
    # Verify association
    assert association.student_id == new_student.id
    assert association.course_id == new_course.id

def test_student_email_uniqueness(setup_database):
    """Test that two students cannot have the same email."""
    session = setup_database
    first_student = Student(name="Jane Doe", email="jane@example.com")
    second_student = Student(name="Mark Smith", email="jane@example.com")
    session.add(first_student)
    session.commit()
    
    session.add(second_student)
    with pytest.raises(IntegrityError):
        session.commit()
    session.rollback()  # Rollback to prevent state leakage between tests
```