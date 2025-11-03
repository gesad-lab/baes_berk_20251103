```python
import pytest
from src.models.course import Course
from src.models.teacher import Teacher
from src.repositories.course_repository import CourseRepository
from src.repositories.teacher_repository import TeacherRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.db.migrations import run_migrations, rollback_migrations

# Setting up a test database engine
TEST_DATABASE_URL = "sqlite:///:memory:"  # In-memory database for testing
engine = create_engine(TEST_DATABASE_URL)
Session = sessionmaker(bind=engine)

@pytest.fixture(scope='module')
def setup_database():
    # Create a new session for the tests
    session = Session()
    run_migrations(engine)  # Set up the database schema
    yield session
    rollback_migrations(engine)  # Clean up after tests


@pytest.fixture
def course_repository(setup_database):
    return CourseRepository(setup_database)


@pytest.fixture
def teacher_repository(setup_database):
    return TeacherRepository(setup_database)


@pytest.fixture
def sample_teacher(teacher_repository):
    teacher = Teacher(name="John Doe", email="john.doe@example.com")
    teacher_repository.add_teacher(teacher)
    return teacher


@pytest.fixture
def sample_course(course_repository):
    course = Course(title="Math 101")
    course_repository.add_course(course)
    return course


def test_assign_teacher_to_course(sample_course, sample_teacher, course_repository):
    """Test assigning a teacher to a course."""
    course_repository.assign_teacher(sample_course.id, sample_teacher.id)
    updated_course = course_repository.get_course_with_teacher(sample_course.id)
    
    assert updated_course.teacher_id == sample_teacher.id
    assert updated_course.teacher.name == sample_teacher.name
    assert updated_course.teacher.email == sample_teacher.email


def test_retrieve_course_with_teacher_details(sample_course, sample_teacher, course_repository):
    """Test retrieving course information with associated teacher details."""
    course_repository.assign_teacher(sample_course.id, sample_teacher.id)
    course_details = course_repository.get_course_with_teacher(sample_course.id)

    assert course_details.title == sample_course.title
    assert course_details.teacher is not None
    assert course_details.teacher.name == sample_teacher.name


def test_assign_teacher_to_non_existent_course(course_repository, sample_teacher):
    """Test assigning a teacher to a non-existent course raises an error."""
    with pytest.raises(ValueError) as excinfo:
        course_repository.assign_teacher(999, sample_teacher.id)  # 999 is an invalid course ID
    assert str(excinfo.value) == "Course does not exist."


def test_retrieve_course_without_assigned_teacher(course_repository):
    """Test retrieving a course that has no assigned teacher."""
    course = Course(title="Science 101")
    course_repository.add_course(course)
    course_details = course_repository.get_course_with_teacher(course.id)

    assert course_details.title == course.title
    assert course_details.teacher is None
```