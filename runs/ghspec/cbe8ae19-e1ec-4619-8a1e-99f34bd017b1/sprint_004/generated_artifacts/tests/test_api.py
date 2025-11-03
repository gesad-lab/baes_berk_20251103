```python
import pytest
from app import create_app, db
from models import Course, Student  # Assuming Student model is defined
from services.course_service import CourseService
from services.student_course_service import associate_courses_with_student, get_student_courses, list_students_with_courses

@pytest.fixture
def setup_database():
    """Setup a test database before each test."""
    db.create_all()  # Create the database tables
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Drop all tables after tests

@pytest.fixture
def course_service(setup_database):
    """Fixture for the CourseService."""
    return CourseService()

@pytest.fixture
def student_data():
    """Helper fixture to create a sample student."""
    student = Student(name="John Doe", email="john.doe@example.com")
    db.session.add(student)
    db.session.commit()
    return student

@pytest.fixture
def course_data():
    """Fixture providing sample course data."""
    course1 = Course(name="Intro to Python", level="Beginner")
    course2 = Course(name="Data Structures", level="Intermediate")
    db.session.add_all([course1, course2])
    db.session.commit()
    return [course1, course2]

def test_associate_courses_with_student(setup_database, student_data, course_data):
    """Test associating courses with a student."""
    response = associate_courses_with_student(student_data.id, [course_data[0].id, course_data[1].id])
    assert response['message'] == "Courses associated successfully."
    
    # Retrieve and verify
    enrolled_courses = get_student_courses(student_data.id)
    assert len(enrolled_courses) == 2
    assert enrolled_courses[0]['name'] == course_data[0].name
    assert enrolled_courses[1]['name'] == course_data[1].name

def test_get_student_courses(setup_database, student_data, course_data):
    """Test retrieving courses associated with a student."""
    associate_courses_with_student(student_data.id, [course_data[0].id, course_data[1].id])
    courses = get_student_courses(student_data.id)
    
    assert len(courses) == 2
    assert all(course['level'] in ['Beginner', 'Intermediate'] for course in courses)

def test_list_students_with_courses(setup_database, student_data, course_data):
    """Test retrieving all students with their associated courses."""
    associate_courses_with_student(student_data.id, [course_data[0].id])
    
    student_courses_list = list_students_with_courses()
    assert len(student_courses_list) == 1
    assert student_courses_list[0]['student']['name'] == student_data.name
    assert len(student_courses_list[0]['courses']) == 1
    assert student_courses_list[0]['courses'][0]['name'] == course_data[0].name
```