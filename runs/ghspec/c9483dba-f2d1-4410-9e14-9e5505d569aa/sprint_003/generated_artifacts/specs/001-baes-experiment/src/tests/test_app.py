```python
import pytest
from app import app  # Assuming 'app' is the Flask app instance
from models import Course  # Assuming 'Course' model is defined in 'models.py'

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_course_success(client):
    """Test creating a course with valid name and level."""
    response = client.post('/courses', json={'name': 'Mathematics 101', 'level': 'Beginner'})
    assert response.status_code == 201
    response_data = response.get_json()
    assert 'id' in response_data
    assert response_data['name'] == 'Mathematics 101'
    assert response_data['level'] == 'Beginner'

def test_create_course_missing_name(client):
    """Test creating a course without a name."""
    response = client.post('/courses', json={'level': 'Beginner'})
    assert response.status_code == 400
    response_data = response.get_json()
    assert response_data == {"error": {"code": "E001", "message": "Name and Level are required"}}

def test_create_course_missing_level(client):
    """Test creating a course without a level."""
    response = client.post('/courses', json={'name': 'Mathematics 101'})
    assert response.status_code == 400
    response_data = response.get_json()
    assert response_data == {"error": {"code": "E001", "message": "Name and Level are required"}}

def test_get_course_success(client):
    """Test retrieving a course by valid ID."""
    # First, create a course to retrieve
    post_response = client.post('/courses', json={'name': 'Biology 101', 'level': 'Intermediate'})
    course_id = post_response.get_json()['id']
    
    # Now, retrieve the course
    response = client.get(f'/courses/{course_id}')
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['id'] == course_id
    assert response_data['name'] == 'Biology 101'
    assert response_data['level'] == 'Intermediate'

def test_get_course_not_found(client):
    """Test retrieving a course by ID that does not exist."""
    response = client.get('/courses/9999')  # Assuming 9999 does not exist
    assert response.status_code == 404
```