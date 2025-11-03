import pytest
from flask import json
from src.app import create_app, db
from src.models.course import Course

@pytest.fixture
def app():
    """Fixture for creating a Flask application with test configuration."""
    app = create_app({'TESTING': True})
    
    with app.app_context():
        # Create the database and tables
        db.create_all()
        yield app
        # Drop the database after tests are finished
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture for the test client."""
    return app.test_client()

def test_create_course(client):
    """Test creating a course with valid data."""
    response = client.post('/courses', json={"name": "Introduction to Programming", "level": "Beginner"})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == "Introduction to Programming"
    assert data['level'] == "Beginner"

def test_create_course_without_name(client):
    """Test creating a course without a name."""
    response = client.post('/courses', json={"level": "Beginner"})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == "E001"
    assert data['error']['message'] == "Name field is required."

def test_create_course_without_level(client):
    """Test creating a course without a level."""
    response = client.post('/courses', json={"name": "Introduction to Programming"})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == "E002"
    assert data['error']['message'] == "Level field is required."

def test_get_courses_empty(client):
    """Test retrieving courses when no courses exist."""
    response = client.get('/courses')
    assert response.status_code == 200
    data = response.get_json()
    assert data == []  # Expecting an empty list

def test_get_courses(client):
    """Test retrieving courses after adding a course."""
    client.post('/courses', json={"name": "Introduction to Programming", "level": "Beginner"})
    response = client.get('/courses')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['name'] == "Introduction to Programming"
    assert data[0]['level'] == "Beginner"