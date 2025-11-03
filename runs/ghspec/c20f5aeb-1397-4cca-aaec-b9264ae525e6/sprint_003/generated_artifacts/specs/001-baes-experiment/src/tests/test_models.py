```python
import pytest
from src.database import get_db, init_db
from src.app import create_app
from src.models import Course

@pytest.fixture
def app():
    """Create a new Flask application instance for testing."""
    app = create_app({"TESTING": True})
    with app.app_context():
        init_db()  # Initialize the database with the schema
    yield app

@pytest.fixture
def client(app):
    """Create a test client for the application."""
    return app.test_client()

def test_course_model_creation():
    """Test that Course model can be created with valid data."""
    course = Course(name="Sample Course", level="Intermediate")
    assert course.name == "Sample Course"
    assert course.level == "Intermediate"

def test_course_model_creation_with_missing_name():
    """Test that Course model raises error when name is missing."""
    with pytest.raises(ValueError) as exc_info:
        Course(name="", level="Intermediate")
    assert str(exc_info.value) == "Course name is required."

def test_course_model_creation_with_missing_level():
    """Test that Course model raises error when level is missing."""
    with pytest.raises(ValueError) as exc_info:
        Course(name="Sample Course", level="")
    assert str(exc_info.value) == "Course level is required."

def test_course_retrieval(client):
    """Test retrieval of created course entity."""
    course_data = {"name": "Advanced Science", "level": "Advanced"}
    response = client.post('/courses', json=course_data)
    assert response.status_code == 201
    created_course_id = response.get_json()['id']

    response = client.get(f'/courses/{created_course_id}')
    assert response.status_code == 200
    assert response.get_json()['name'] == course_data['name']
    assert response.get_json()['level'] == course_data['level']

def test_create_course_with_invalid_data(client):
    """Test that creating a course with missing name returns a 400 error."""
    response = client.post('/courses', json={
        "name": "",
        "level": "Beginner"
    })
    assert response.status_code == 400
    assert 'error' in response.get_json()
    assert response.get_json()['error']['message'] == "Both name and level fields are required."
```