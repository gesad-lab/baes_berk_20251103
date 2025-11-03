```python
import pytest
from src.models.course import Course
from src.repositories.course_repository import CourseRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.db.migrations import run_migrations, rollback_migrations

# Setting up a test database engine
TEST_DATABASE_URL = "sqlite:///:memory:"  # In-memory database for testing
engine = create_engine(TEST_DATABASE_URL)
Session = sessionmaker(bind=engine)

@pytest.fixture(scope='module')
def test_client():
    """Set up the in-memory test database and apply migrations."""
    with engine.connect() as connection:
        run_migrations(connection)
        yield connection  # This is where the testing happens
        rollback_migrations(connection)

@pytest.fixture
def course_repository():
    """Fixture to provide a CourseRepository instance."""
    session = Session()
    return CourseRepository(session)

def test_assign_teacher_to_course(course_repository):
    """Tests assigning a teacher to a course."""
    # Arrange
    course = Course(name='Test Course', description='A course for testing')
    course_repository.session.add(course)
    course_repository.session.commit()

    # Act
    teacher_id = 1  # Assuming teacher with ID 1 exists for this test
    updated_course = course_repository.assign_teacher(course.id, teacher_id)

    # Assert
    assert updated_course.teacher_id == teacher_id

def test_get_course_with_teacher(course_repository):
    """Tests retrieving a course with its assigned teacher."""
    # Arrange
    course = Course(name='Retrieve Test Course', description='A course to retrieve')
    teacher_id = 2  # Assuming teacher with ID 2 exists for this test
    course.teacher_id = teacher_id
    course_repository.session.add(course)
    course_repository.session.commit()

    # Act
    retrieved_course = course_repository.get_course_with_teacher(course.id)

    # Assert
    assert retrieved_course is not None
    assert retrieved_course.teacher_id == teacher_id
    assert retrieved_course.name == 'Retrieve Test Course'
    assert retrieved_course.description == 'A course to retrieve'
```