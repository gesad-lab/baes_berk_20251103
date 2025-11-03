```python
import pytest
from src.services import assign_teacher_to_course
from src.models import Teacher, Course
from src.database import get_db_session

@pytest.fixture
def db_session():
    """Provides a transactional scope around a test, rolling back at the end."""
    session = get_db_session()
    yield session
    session.rollback()

@pytest.fixture
def sample_teacher_data(db_session):
    """Create sample teacher data for testing."""
    teacher = Teacher(name="John Doe", email="john.doe@example.com")
    db_session.add(teacher)
    db_session.commit()
    return teacher

@pytest.fixture
def sample_course_data(db_session):
    """Create sample course data for testing."""
    course = Course(title="Mathematics 101")
    db_session.add(course)
    db_session.commit()
    return course

def test_assign_teacher_to_course_success(db_session, sample_teacher_data, sample_course_data):
    """Test assigning a teacher to a course successfully."""
    assignment_result = assign_teacher_to_course(course_id=sample_course_data.id, teacher_id=sample_teacher_data.id, db_session=db_session)
    assert assignment_result is True

    # Verify the teacher is now associated with the course
    course = db_session.query(Course).filter_by(id=sample_course_data.id).first()
    assert course.teacher_id == sample_teacher_data.id

def test_assign_teacher_to_nonexistent_course(db_session, sample_teacher_data):
    """Test assignment of a teacher to a non-existent course."""
    with pytest.raises(ValueError) as excinfo:
        assign_teacher_to_course(course_id=9999, teacher_id=sample_teacher_data.id, db_session=db_session)
    assert "Course not found" in str(excinfo.value)

def test_assign_nonexistent_teacher_to_course(db_session, sample_course_data):
    """Test assignment of a non-existent teacher to a course."""
    with pytest.raises(ValueError) as excinfo:
        assign_teacher_to_course(course_id=sample_course_data.id, teacher_id=9999, db_session=db_session)
    assert "Teacher not found" in str(excinfo.value)

def test_assign_teacher_to_course_when_already_assigned(db_session, sample_teacher_data, sample_course_data):
    """Test assignment of a teacher to a course when the teacher is already assigned to that course."""
    assign_teacher_to_course(course_id=sample_course_data.id, teacher_id=sample_teacher_data.id, db_session=db_session)  # First assignment

    with pytest.raises(ValueError) as excinfo:
        assign_teacher_to_course(course_id=sample_course_data.id, teacher_id=sample_teacher_data.id, db_session=db_session)  # Second assignment
    assert "Teacher already assigned to this course" in str(excinfo.value)
```