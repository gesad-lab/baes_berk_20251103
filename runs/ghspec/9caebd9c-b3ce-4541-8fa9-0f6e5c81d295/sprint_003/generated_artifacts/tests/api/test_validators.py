```python
import json
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from your_application import app, db, Course  # Adjust import based on your structure

# Reinitialize the Flask application and SQLAlchemy for testing
@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables for testing
        yield client  # This will run the tests

def test_create_course_valid(test_client):
    """Test creating a course with valid data"""
    response = test_client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json['message'] == "Course created successfully"
    assert 'course_id' in response.json  # Ensure a course ID is returned

def test_create_course_missing_fields(test_client):
    """Test creating a course without required fields"""
    response = test_client.post('/courses', json={"name": "", "level": ""})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"  # Error code for missing fields
    assert response.json['error']['message'] == "Both name and level are required."  # Assuming appropriate message

def test_create_course_missing_name(test_client):
    """Test creating a course with missing name"""
    response = test_client.post('/courses', json={"name": "", "level": "Intermediate"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"
    assert response.json['error']['message'] == "Name is required."  # Assuming appropriate message

def test_create_course_missing_level(test_client):
    """Test creating a course with missing level"""
    response = test_client.post('/courses', json={"name": "Math 201", "level": ""})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"
    assert response.json['error']['message'] == "Level is required."  # Assuming appropriate message

def test_retrieve_course_details(test_client):
    """Test retrieving the details of a created course"""
    # First, create a course to retrieve
    creation_response = test_client.post('/courses', json={"name": "Science 101", "level": "Beginner"})
    course_id = creation_response.json['course_id']
    
    # Now, retrieve the course details
    response = test_client.get(f'/courses/{course_id}')
    assert response.status_code == 200
    assert response.json['name'] == "Science 101"
    assert response.json['level'] == "Beginner"
```