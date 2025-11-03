import pytest
from app import create_app, db
from models.course import Course

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')  # Initialize app with testing configuration
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()  # Create the database and all tables

        yield testing_client  # This is where the testing happens!

        db.drop_all()  # Teardown after tests

def test_create_course_success(test_client):
    """Test creating a course with valid input."""
    response = test_client.post('/courses', json={'name': 'Math 101', 'level': 'Beginner'})
    assert response.status_code == 201
    assert 'name' in response.json
    assert 'level' in response.json
    assert response.json['name'] == 'Math 101'
    assert response.json['level'] == 'Beginner'

def test_create_course_missing_field(test_client):
    """Test creating a course without required fields."""
    response = test_client.post('/courses', json={'name': 'Math 101'})  # Missing 'level'
    assert response.status_code == 400
    assert response.json['error']['message'] == "Both 'name' and 'level' are required."

def test_get_all_courses(test_client):
    """Test retrieving all courses."""
    # Create a course to retrieve
    test_client.post('/courses', json={'name': 'Math 101', 'level': 'Beginner'})
    test_client.post('/courses', json={'name': 'Science 101', 'level': 'Intermediate'})
    
    response = test_client.get('/courses')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) >= 2  # Expect at least two courses created above

def test_database_migration(test_client):
    """Test if the Course table was created and is empty initially."""
    with app.app_context():
        courses = Course.query.all()
        assert len(courses) == 0  # Initially, no courses should be present in the database

        # Add a course and check again
        test_client.post('/courses', json={'name': 'History 101', 'level': 'Advanced'})
        courses = Course.query.all()
        assert len(courses) == 1  # Now one course should be present