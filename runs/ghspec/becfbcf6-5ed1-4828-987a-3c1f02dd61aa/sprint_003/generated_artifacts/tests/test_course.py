```python
import pytest
from app import app, db, Course

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for testing
            # Adding a sample course for retrieval tests
            course1 = Course(name="Introduction to Python", level="Beginner")
            course2 = Course(name="Advanced Java", level="Advanced")
            db.session.add(course1)
            db.session.add(course2)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after the tests

def test_retrieve_all_courses(client):
    """Test retrieving all courses."""
    response = client.get('/courses')
    assert response.status_code == 200
    courses = response.get_json()
    assert isinstance(courses, list)  # Should be a list
    assert len(courses) == 2  # We added 2 courses for this test
    assert courses[0]['name'] == "Introduction to Python"
    assert courses[1]['name'] == "Advanced Java"
    assert 'id' in courses[0]  # Check for presence of ID
    assert 'level' in courses[1]  # Check for presence of level
```