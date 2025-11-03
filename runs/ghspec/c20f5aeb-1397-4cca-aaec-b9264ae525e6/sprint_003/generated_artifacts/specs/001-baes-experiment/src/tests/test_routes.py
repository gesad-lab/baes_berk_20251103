```python
import json
import time
import pytest
from app import app, db
from models import Student

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables
        yield client
        db.drop_all()  # Cleanup after each test

def test_create_student_with_email_response_time(client):
    """Test that creating a student with an email responds within 2 seconds."""
    start_time = time.time()
    response = client.post('/students', json={"email": "test@example.com"})
    assert response.status_code == 201
    assert response.get_json()['email'] == "test@example.com"
    assert time.time() - start_time < 2

def test_create_course_with_valid_data(client):
    """Test that creating a course with valid inputs succeeds."""
    response = client.post('/courses', json={
        "name": "Introduction to Programming",
        "level": "Beginner"
    })
    assert response.status_code == 201
    assert 'id' in response.get_json()
    assert response.get_json()['name'] == "Introduction to Programming"
    assert response.get_json()['level'] == "Beginner"

def test_create_course_with_missing_name(client):
    """Test that attempting to create a course without a name field returns a 400 error."""
    response = client.post('/courses', json={
        "name": "",
        "level": "Beginner"
    })
    assert response.status_code == 400
    assert 'error' in response.get_json()
    assert response.get_json()['error']['code'] == 'E001'
    assert response.get_json()['error']['message'] == 'Name field is required.'

def test_create_course_with_missing_level(client):
    """Test that attempting to create a course without a level field returns a 400 error."""
    response = client.post('/courses', json={
        "name": "Introduction to Programming",
        "level": ""
    })
    assert response.status_code == 400
    assert 'error' in response.get_json()
    assert response.get_json()['error']['code'] == 'E001'
    assert response.get_json()['error']['message'] == 'Level field is required.'

def test_create_course_with_invalid_data(client):
    """Test that creating a course with invalid data returns a 400 error."""
    response = client.post('/courses', json={
        "name": None,
        "level": None
    })
    assert response.status_code == 400
    assert 'error' in response.get_json()
    assert response.get_json()['error']['code'] == 'E001'
    assert response.get_json()['error']['message'] == 'Both name and level fields cannot be empty.'
```