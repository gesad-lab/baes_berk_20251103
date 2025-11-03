```python
import pytest
from src.database import get_db, init_db
from src.models import Student, Course
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test

def test_course_creation(db):
    """Test creating a new course record."""
    course = Course(name="Mathematics", level="Beginner")
    db.session.add(course)
    db.session.commit()
    
    assert course.id is not None
    assert course.name == "Mathematics"
    assert course.level == "Beginner"

def test_course_creation_without_name(db):
    """Test creating a course without a name raises an error."""
    course = Course(level="Beginner")
    db.session.add(course)

    with pytest.raises(IntegrityError):
        db.session.commit()
        db.session.rollback()  # Rollback changes after the test

def test_course_creation_without_level(db):
    """Test creating a course without a level raises an error."""
    course = Course(name="Science")
    db.session.add(course)

    with pytest.raises(IntegrityError):
        db.session.commit()
        db.session.rollback()  # Rollback changes after the test

def test_duplicate_course_names(db):
    """Test creating duplicate course names raises an error."""
    course1 = Course(name="Physics", level="Intermediate")
    course2 = Course(name="Physics", level="Advanced")  # Same name, different level
    db.session.add(course1)
    db.session.commit()
    
    db.session.add(course2)
    with pytest.raises(IntegrityError):
        db.session.commit()
        db.session.rollback()  # Rollback changes after the test
```