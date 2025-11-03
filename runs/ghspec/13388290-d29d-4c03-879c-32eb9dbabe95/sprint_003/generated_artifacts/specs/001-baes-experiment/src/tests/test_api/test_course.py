```python
import pytest
from app import create_app, db
from app.models import Course
from http import HTTPStatus

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create schema for testing
            # Create a sample course for testing retrieval
            new_course = Course(name="Test Course", level="Advanced")
            db.session.add(new_course)
            db.session.commit()
        yield client

def test_create_course(client):
    """Test successful creation of a course with valid data."""
    response = client.post('/courses', json={"name": "Mathematics 101", "level": "Beginner"})
    assert response.status_code == HTTPStatus.CREATED
    assert response.json['name'] == "Mathematics 101"
    assert response.json['level'] == "Beginner"

def test_create_course_without_fields(client):
    """Test creation of a course without required fields returns an error."""
    response = client.post('/courses', json={"name": ""})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json['error']['code'] == 'E001'  # Validate error code for missing fields

def test_get_course_details(client):
    """Test successful retrieval of course details by ID."""
    # Assuming the course was created earlier in the fixture
    course = Course.query.first()
    response = client.get(f'/courses/{course.id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json['id'] == course.id
    assert response.json['name'] == course.name
    assert response.json['level'] == course.level

def test_get_nonexistent_course(client):
    """Test retrieval of a course that does not exist returns a 404 error."""
    response = client.get('/courses/99999')  # Assuming this ID does not exist
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json['error']['code'] == 'E002'  # Example error code for not found
```