```python
import pytest
from models import db, Course, Teacher
from services.course_service import assign_teacher_to_course, get_course_details

@pytest.fixture
def setup_database():
    """Setup a test database before each test."""
    db.create_all()  # Create the database tables
    # Create a sample teacher and course for testing
    teacher = Teacher(name="John Doe", email="john.doe@example.com")
    course = Course(title="Introduction to Testing", description="Learn how to write tests.")
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()  # Save changes to the database
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Cleanup the database

def test_assign_teacher_to_course(setup_database):
    """Test assigning a teacher to a course successfully."""
    course = Course.query.first()
    teacher = Teacher.query.first()
    
    # Assign the teacher to the course
    result = assign_teacher_to_course(course.id, teacher.id)
    
    # Verify that the assignment was successful
    assert result is True
    assert course.teacher_id == teacher.id  # Check that the course now has the teacher assigned

def test_assign_teacher_to_nonexistent_course(setup_database):
    """Test assigning a teacher to a non-existent course returns False."""
    teacher = Teacher.query.first()
    result = assign_teacher_to_course(999, teacher.id)  # Trying to assign a teacher to a non-existent course
    
    assert result is False  # Expecting the operation to fail

def test_get_course_details_with_teacher(setup_database):
    """Test retrieving course details including the assigned teacher."""
    course = Course.query.first()
    teacher = Teacher.query.first()
    
    # Assign the teacher to the course
    assign_teacher_to_course(course.id, teacher.id)
    
    # Retrieve course details
    course_details = get_course_details(course.id)
    
    # Verify that the course details include teacher information
    assert course_details['title'] == course.title
    assert course_details['teacher_id'] == teacher.id  # Ensure the teacher is correctly assigned

def test_get_details_for_nonexistent_course(setup_database):
    """Test retrieval of details for a non-existent course returns None."""
    course_details = get_course_details(999)  # Trying to get details for a non-existent course
    
    assert course_details is None  # Expecting None for a non-existent course
```