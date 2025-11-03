```python
import pytest
from src.models import Course, Teacher  # Import both Course and Teacher models for testing
from src.database import get_db, init_db
from src.app import create_app

@pytest.fixture
def app():
    """Create a new Flask application instance for testing."""
    app = create_app({"TESTING": True})
    with app.app_context():
        init_db()  # Initialize the database with the schema
    yield app

@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    with app.test_client() as client:
        yield client

def test_course_teacher_relationship(client):
    """Test the relationship between Course and Teacher entities."""
    # First create a Teacher
    teacher = Teacher(name="Jane Doe", email="jane.doe@example.com")
    teacher.save()  # Assuming 'save' method exists to insert into the database

    # Create a Course
    course = Course(title="Biology", description="Intro to Biology", teacher_id=teacher.id)
    course.save()  # Assuming 'save' method exists to insert into the database

    # Validate Course instance
    assert course.teacher_id == teacher.id
    assert course.teacher.name == teacher.name  # Assuming a relationship back to Teacher exists

def test_course_teacher_invalid_id(client):
    """Test assigning a Teacher with an invalid ID to a Course raises an error."""
    # Create a Course without a valid Teacher
    course = Course(title="Chemistry", description="Intro to Chemistry")
    course.save()

    # Attempt to assign an invalid teacher_id
    invalid_teacher_id = 99999  # Assuming this ID does not exist in the Teacher table
    response = client.post(f'/courses/{course.id}/assign-teacher', json={"teacher_id": invalid_teacher_id})
    
    # Check if the response indicates an error
    assert response.status_code == 404  # Assuming it returns 404 for not found
    assert response.get_json() == {"error": {"code": "E002", "message": "Teacher not found", "details": {}}}

def test_course_retrieval_with_teacher(client):
    """Test retrieval of a Course along with its Teacher details."""
    # Create a Teacher and Course
    teacher = Teacher(name="Mark Smith", email="mark.smith@example.com")
    teacher.save()

    course = Course(title="Physics", description="Intro to Physics", teacher_id=teacher.id)
    course.save()

    # Retrieve the Course
    response = client.get(f'/courses/{course.id}')
    
    # Validate response structure
    assert response.status_code == 200
    course_data = response.get_json()
    assert course_data['id'] == course.id
    assert course_data['title'] == course.title
    assert course_data['description'] == course.description
    assert course_data['teacher']['id'] == teacher.id
    assert course_data['teacher']['name'] == teacher.name
    assert course_data['teacher']['email'] == teacher.email
```