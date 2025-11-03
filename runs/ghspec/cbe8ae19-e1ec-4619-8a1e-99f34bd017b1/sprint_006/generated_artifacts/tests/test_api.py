```python
import pytest
from app import create_app, db
from models import Course, Teacher
from services.course_service import assign_teacher_to_course, get_course_details

@pytest.fixture
def setup_database():
    """Setup a test database before each test."""
    db.create_all()  # Create the database tables
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Drop all tables after tests

def test_assign_teacher_to_course(setup_database):
    """Test assigning a teacher to a course."""
    # Create a teacher and course for testing
    teacher = Teacher(name="John Doe", email="john.doe@example.com")
    db.session.add(teacher)
    
    course = Course(title="Biology 101")
    db.session.add(course)
    db.session.commit()  # Commit changes to the database

    # Assign teacher to course
    response = assign_teacher_to_course(course.id, teacher.id)
    
    # Check that the assignment was successful
    assert response is True  # Assuming the function returns True on success

    # Verify that the course now has the correct teacher assigned
    updated_course = Course.query.get(course.id)
    assert updated_course.teacher_id == teacher.id

def test_get_course_details_with_teacher(setup_database):
    """Test retrieving course details along with assigned teacher."""
    # Create a teacher and course
    teacher = Teacher(name="Jane Smith", email="jane.smith@example.com")
    db.session.add(teacher)
    
    course = Course(title="Mathematics 101")
    db.session.add(course)
    db.session.commit()

    # Assign teacher to the course
    assign_teacher_to_course(course.id, teacher.id)

    # Retrieve course details
    course_details = get_course_details(course.id)

    # Check that the course details include the teacher
    assert course_details['title'] == course.title
    assert course_details['teacher']['id'] == teacher.id
    assert course_details['teacher']['name'] == teacher.name
```