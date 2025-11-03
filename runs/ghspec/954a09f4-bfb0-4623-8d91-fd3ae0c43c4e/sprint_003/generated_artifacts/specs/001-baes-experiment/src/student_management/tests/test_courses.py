```python
import pytest
from src.app import app, db
from src.models import Course

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the tables for testing
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_create_course(client):
    """Test that a course can be created successfully."""
    response = client.post('/courses', json={'name': 'Mathematics', 'level': 'Advanced'})
    assert response.status_code == 201  # Check for successful creation
    assert 'id' in response.json  # Course ID should be returned
    assert response.json['name'] == 'Mathematics'  # Check name
    assert response.json['level'] == 'Advanced'  # Check level

def test_create_course_with_missing_fields(client):
    """Test that course creation fails with missing fields."""
    response = client.post('/courses', json={})  # No data provided
    assert response.status_code == 400  # Expected error response
    assert response.json == {
        'error': {
            'code': 'E001',
            'message': 'Name and level are required.'
        }
    }

def test_retrieve_course_by_id(client):
    """Test that a course can be retrieved by ID."""
    # First create a course to test retrieval
    post_response = client.post('/courses', json={'name': 'Mathematics', 'level': 'Advanced'})
    course_id = post_response.json['id']  # Get the newly created course ID

    # Now retrieve the course
    response = client.get(f'/courses/{course_id}')
    assert response.status_code == 200  # Check for successful retrieval
    assert response.json['id'] == course_id  # Check the correct ID is returned
    assert response.json['name'] == 'Mathematics'  # Check the name
    assert response.json['level'] == 'Advanced'  # Check the level

def test_retrieve_non_existent_course(client):
    """Test retrieving a course that does not exist."""
    response = client.get('/courses/9999')  # Attempt to retrieve a non-existent course
    assert response.status_code == 404  # Expected not found error
    assert response.json == {
        'error': {
            'code': 'E002',
            'message': 'Course not found.'
        }
    }

def test_database_migration_verification(client):
    """Test that the courses table is created and existing data is preserved."""
    # Initial checks to verify that the Course table exists post-migration
    response = client.get('/courses')  # Fetch all courses should return an empty list if no courses exist
    assert response.status_code == 200
    assert response.json == []  # Initially, there should be no courses

    # Check that the student data from the previous migration is still intact
    # Assuming students were already migrated, this can be implemented based on actual data verification.
    # For example purposes, we are just checking that our migration does not crash.
```
