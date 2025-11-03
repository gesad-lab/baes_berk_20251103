```python
import pytest
from flask import json
from src.database import get_db, init_db
from src.models import Course

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test

def test_create_course(db):
    """Test creating a new course record."""
    # Define the course data to be sent in the POST request
    course_data = {
        "name": "Introduction to Programming",
        "level": "Beginner"
    }
    
    # Simulate a POST request to create a new course
    response = db.session.post('/courses', json=course_data)
    
    # Check the response status code and content
    assert response.status_code == 201  # Expected HTTP status code for created
    response_data = response.get_json()
    
    # Verify that the response contains the expected fields
    assert "id" in response_data
    assert response_data["name"] == course_data["name"]
    assert response_data["level"] == course_data["level"]

def test_get_course_by_id(db):
    """Test retrieving a created course by ID."""
    # First, create a course to retrieve
    course_data = {
        "name": "Data Structures",
        "level": "Intermediate"
    }
    
    create_response = db.session.post('/courses', json=course_data)
    new_course = create_response.get_json()
    
    # Simulate a GET request to retrieve the created course using its ID
    response = db.session.get(f'/courses/{new_course["id"]}')
    
    # Check the response status code and content
    assert response.status_code == 200  # Expected HTTP status code for OK
    response_data = response.get_json()
    
    # Verify that the retrieved course matches the created course
    assert response_data["id"] == new_course["id"]
    assert response_data["name"] == course_data["name"]
    assert response_data["level"] == course_data["level"]

def test_get_all_courses(db):
    """Test retrieving a list of all courses."""
    # Create multiple courses for testing
    courses_data = [
        {"name": "Machine Learning", "level": "Advanced"},
        {"name": "Web Development", "level": "Beginner"}
    ]
    
    for course_data in courses_data:
        db.session.post('/courses', json=course_data)
    
    # Simulate a GET request to retrieve all courses
    response = db.session.get('/courses')
    
    # Check the response status code
    assert response.status_code == 200  # Expected HTTP status code for OK
    response_data = response.get_json()
    
    # Check that the response contains the correct number of courses
    assert len(response_data) == len(courses_data) + 1  # Include previously created course in tests

```