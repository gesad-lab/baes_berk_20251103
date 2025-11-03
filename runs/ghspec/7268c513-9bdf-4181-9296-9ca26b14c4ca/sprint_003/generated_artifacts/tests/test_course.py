```python
import pytest
from flask import json
from app import create_app, db  # Assuming create_app sets up the Flask app and db is the SQLAlchemy instance
from app.models import Course  # Assuming the Course model is defined in models.py

@pytest.fixture
def client():
    app = create_app({'TESTING': True})  # Create a test instance of the application
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
        yield client

def test_create_course(client):
    # Test creating a course with valid data
    response = client.post('/courses', json={
        "name": "Mathematics",
        "level": "Intermediate"
    })
    assert response.status_code == 201
    assert response.json['name'] == "Mathematics"
    assert response.json['level'] == "Intermediate"

def test_create_course_missing_name(client):
    # Test creating a course with missing name
    response = client.post('/courses', json={"level": "Intermediate"})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E001", "message": "Name and level are required."}}

def test_create_course_missing_level(client):
    # Test creating a course with missing level
    response = client.post('/courses', json={"name": "Mathematics"})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E001", "message": "Name and level are required."}}

def test_get_courses(client):
    # Ensure that we can retrieve courses
    response = client.get('/courses')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Should return a list of courses
```