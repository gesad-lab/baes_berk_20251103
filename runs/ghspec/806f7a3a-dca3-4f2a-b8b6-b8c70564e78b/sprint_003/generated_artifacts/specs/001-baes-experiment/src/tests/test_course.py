```python
import pytest
from flask import json
from app import create_app, db
from models.course import Course  # Import the Course model

@pytest.fixture
def client():
    app = create_app('testing')  # Use a separate testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create fresh database for each test
        yield client
        with app.app_context():
            db.drop_all()  # Clean up database after tests

def test_create_course(client):
    """Test the creation of a course with valid data."""
    response = client.post('/courses', 
                            data=json.dumps({'name': 'Mathematics', 'level': 'Beginner'}),
                            content_type='application/json')
    assert response.status_code == 201  # Check if creation was successful
    data = json.loads(response.data)
    assert data['course']['name'] == 'Mathematics'  # Verify course name
    assert data['course']['level'] == 'Beginner'  # Verify course level

def test_get_course(client):
    """Test retrieving a course by its ID."""
    course = Course(name='Physics', level='Intermediate')
    db.session.add(course)
    db.session.commit()
    
    response = client.get(f'/courses/{course.id}')
    assert response.status_code == 200  # Check if retrieval was successful
    data = json.loads(response.data)
    assert data['course']['name'] == 'Physics'  # Verify course name
    assert data['course']['level'] == 'Intermediate'  # Verify course level

def test_update_course(client):
    """Test updating a course's name."""
    course = Course(name='Chemistry', level='Advanced')
    db.session.add(course)
    db.session.commit()

    response = client.put(f'/courses/{course.id}', 
                          data=json.dumps({'name': 'Advanced Chemistry', 'level': 'Advanced'}),
                          content_type='application/json')
    assert response.status_code == 200  # Check if update was successful
    updated_course = Course.query.get(course.id)
    assert updated_course.name == 'Advanced Chemistry'  # Verify updated name

def test_create_course_with_missing_name(client):
    """Test creating a course without a name."""
    response = client.post('/courses', 
                            data=json.dumps({'level': 'Beginner'}),
                            content_type='application/json')
    assert response.status_code == 400  # Check for bad request due to validation
    data = json.loads(response.data)
    assert data['error']['message'] == 'Course name is required'  # Check error message

def test_create_course_with_missing_level(client):
    """Test creating a course without a level."""
    response = client.post('/courses', 
                            data=json.dumps({'name': 'Mathematics'}),
                            content_type='application/json')
    assert response.status_code == 400  # Check for bad request due to validation
    data = json.loads(response.data)
    assert data['error']['message'] == 'Course level is required'  # Check error message
```