```python
import pytest
from flask import json
from your_application import create_app  # import your app factory function
from your_application.models import db, Course  # import db and Course model
from your_application.database import init_db  # import your database initialization function

@pytest.fixture
def app():
    """Create a Flask application for testing."""
    app = create_app('TEST')  # use the testing configuration
    with app.app_context():
        init_db()  # initialize the database for testing
        yield app

@pytest.fixture
def client(app):
    """Create a test client for the application."""
    return app.test_client()

@pytest.fixture
def setup_courses(app):
    """Setup test data in the database before each test."""
    with app.app_context():
        # Add sample courses to the database for testing
        course1 = Course(name='Mathematics', level='Beginner')
        course2 = Course(name='History', level='Intermediate')
        db.session.add(course1)
        db.session.add(course2)
        db.session.commit()

def test_display_all_courses(client, setup_courses):
    """Test retrieving a list of all courses."""
    response = client.get('/courses')  # Assuming endpoint is '/courses'
    assert response.status_code == 200  # Check for successful response
    data = json.loads(response.data)  # Load the response data as JSON
    assert isinstance(data, list)  # Ensure the response is a list
    assert len(data) == 2  # Ensure two courses were returned
    assert data[0] == {'name': 'Mathematics', 'level': 'Beginner'}
    assert data[1] == {'name': 'History', 'level': 'Intermediate'}
```