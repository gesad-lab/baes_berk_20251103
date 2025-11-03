```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Course

# Set up the test database
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database schema
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db_session():
    """Provides a transactional scope around a series of tests."""
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)

    yield session  # This is where the testing happens

    session.close()
    transaction.rollback()
    connection.close()

def test_create_course_with_valid_data(db_session):
    """Test creating a course with valid name and level."""
    course = Course(name="Math 101", level="Beginner")
    db_session.add(course)
    db_session.commit()
    
    assert course.id is not None
    assert course.name == "Math 101"
    assert course.level == "Beginner"

def test_course_validation_with_missing_name(db_session):
    """Test validation failure when creating a course with missing name."""
    course = Course(name="", level="Expert")
    
    # Validation must be handled prior to adding to the session
    assert not Course.validate_name_and_level(course.name, course.level)

def test_course_validation_with_missing_level(db_session):
    """Test validation failure when creating a course with missing level."""
    course = Course(name="Biology 101", level="")
    
    assert not Course.validate_name_and_level(course.name, course.level)

def test_retrieve_course(db_session):
    """Test retrieving a course by its ID."""
    course = Course(name="Physics 101", level="Intermediate")
    db_session.add(course)
    db_session.commit()
    
    retrieved_course = db_session.query(Course).filter(Course.id == course.id).first()
    assert retrieved_course is not None
    assert retrieved_course.name == "Physics 101"
    assert retrieved_course.level == "Intermediate"

def test_update_course(db_session):
    """Test updating the course's name."""
    course = Course(name="Chemistry 101", level="Advanced")
    db_session.add(course)
    db_session.commit()
    
    course.name = "Chemistry 102"  # Update course name
    db_session.commit()
    
    updated_course = db_session.query(Course).filter(Course.id == course.id).first()
    assert updated_course.name == "Chemistry 102"
    assert updated_course.level == "Advanced"
```