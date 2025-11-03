```python
import pytest
from app import create_app, db
from models import Course
from services.course_service import CourseService

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

def test_create_course(course_service):
    """Test creating a new course."""
    course_data = {
        'title': 'Test Course',
        'description': 'A course for testing purposes.',
        'credits': 3
    }
    
    response = course_service.create_course(course_data)
    
    assert response.status_code == 201  # Check if course was created successfully
    assert response.json['title'] == course_data['title']  # Validate response content

def test_get_course_by_id(course_service):
    """Test retrieving a course by ID."""
    # First, create a course to retrieve
    course_data = {
        'title': 'Sample Course',
        'description': 'A sample course description.',
        'credits': 4
    }
    created_course = course_service.create_course(course_data)
    course_id = created_course.json['id']  # Get the ID of the created course

    response = course_service.get_course_by_id(course_id)  # Retrieve course by ID
    
    assert response.status_code == 200  # Check the response status
    assert response.json['id'] == course_id  # Validate the course ID is returned
    assert response.json['title'] == course_data['title']  # Validate title

def test_list_all_courses(course_service):
    """Test listing all courses."""
    # Create multiple courses to test listing
    course_data_1 = {
        'title': 'Course One',
        'description': 'First course description.',
        'credits': 3
    }
    course_data_2 = {
        'title': 'Course Two',
        'description': 'Second course description.',
        'credits': 4
    }
    
    course_service.create_course(course_data_1)
    course_service.create_course(course_data_2)

    response = course_service.list_all_courses()  # List all courses

    assert response.status_code == 200  # Check if listing was successful
    assert len(response.json) >= 2  # Ensure at least two courses are listed
```