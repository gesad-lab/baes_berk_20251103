```python
import pytest
from flask import json
from app import create_app, db
from app.models import Course

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Create the database tables
            # Add a sample course for testing update and listing
            sample_course = Course(name='Sample Course', level='Beginner')
            db.session.add(sample_course)
            db.session.commit()
        yield testing_client  # This is where the testing happens
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_create_course(test_client):
    """Test creating a course."""
    response = test_client.post('/courses', data=json.dumps({
        'name': 'Test Course',
        'level': 'Intermediate'
    }), content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data  # Ensure there's an ID returned
    assert data['name'] == 'Test Course'
    assert data['level'] == 'Intermediate'


def test_list_courses(test_client):
    """Test listing all courses."""
    response = test_client.get('/courses')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)  # Check that the response is a list
    assert len(data) > 0  # Ensure at least one course is returned


def test_update_course(test_client):
    """Test updating an existing course."""
    # Assume the first course has ID 1 added in the fixture above
    response = test_client.put('/courses/1', data=json.dumps({
        'name': 'Updated Course',
        'level': 'Advanced'
    }), content_type='application/json')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Updated Course'
    assert data['level'] == 'Advanced'
```