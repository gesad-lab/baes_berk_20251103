```python
import pytest
from models import db, Course, StudentCourses
from services.student_course_service import associate_student_with_courses, get_courses_for_student, get_all_students_with_courses

@pytest.fixture
def setup_database():
    """Setup a test database before each test."""
    db.create_all()  # Create the database tables
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Drop all tables after tests

@pytest.fixture
def sample_courses():
    """Fixture providing sample course data."""
    course1 = Course(name="Math 101", level="Undergraduate")
    course2 = Course(name="History 101", level="Undergraduate")
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()
    return course1, course2

@pytest.fixture
def associate_students(sample_courses):
    """Associate student data with courses for testing."""
    # Assuming a Student model exists, this would be replaced with actual student creation logic
    student_id = 1  # Placeholder for the actual student ID
    associate_student_with_courses(student_id, [course.id for course in sample_courses])  # Associate courses

def test_associate_student_with_courses(associate_students):
    """Test the association of a student with courses."""
    # Verify the association was successful
    student_courses = db.session.query(StudentCourses).filter_by(student_id=1).all()
    assert len(student_courses) == 2  # Ensure two courses are associated
    assert student_courses[0].course_id in [1, 2]  # Check if associated courses are correct

def test_get_courses_for_student(associate_students):
    """Test retrieval of courses for a specific student."""
    courses = get_courses_for_student(1)  # Assuming 1 is the student's ID
    assert len(courses) == 2
    assert courses[0]['name'] in ["Math 101", "History 101"]

def test_get_all_students_with_courses(associate_students):
    """Test retrieval of all students with their respective courses."""
    all_students_with_courses = get_all_students_with_courses()
    assert len(all_students_with_courses) > 0
    assert '1' in all_students_with_courses  # Check if our test student is present
    assert len(all_students_with_courses['1']) == 2  # Ensure two courses are linked to student
```