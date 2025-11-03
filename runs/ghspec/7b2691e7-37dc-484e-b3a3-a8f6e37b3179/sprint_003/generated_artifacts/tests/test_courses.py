```python
import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError
from api.routes.courses import courses_bp, CourseSchema
from models import Course  # Assuming Course model is defined in models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)
app.register_blueprint(courses_bp)  # Register the courses blueprint

# Create the database tables
with app.app_context():
    db.create_all()

def test_create_course_with_valid_data():
    """Test creating a course with valid name and level values."""
    response = app.test_client().post('/courses', json={
        'name': 'Mathematics',
        'level': 'Beginner'
    })
    assert response.status_code == 201  # Expecting a successful creation
    data = response.get_json()
    assert data['name'] == 'Mathematics'
    assert data['level'] == 'Beginner'
    # Validate that the Course is stored in the database
    course_in_db = Course.query.filter_by(name='Mathematics').first()
    assert course_in_db is not None

def test_create_course_without_name():
    """Test creating a course without providing a name."""
    response = app.test_client().post('/courses', json={
        'level': 'Intermediate'
    })
    assert response.status_code == 400  # Expecting a validation error
    data = response.get_json()
    assert 'error' in data

def test_create_course_without_level():
    """Test creating a course without providing a level."""
    response = app.test_client().post('/courses', json={
        'name': 'Science'
    })
    assert response.status_code == 400  # Expecting a validation error
    data = response.get_json()
    assert 'error' in data

def test_retrieve_course_by_id():
    """Test retrieving a course record by its unique identifier."""
    # First, create a course to retrieve later
    with app.app_context():
        course = Course(name='Physics', level='Advanced')
        db.session.add(course)
        db.session.commit()
    
    response = app.test_client().get(f'/courses/{course.id}')
    assert response.status_code == 200  # Expecting success when getting the course
    data = response.get_json()
    assert data['name'] == 'Physics'
    assert data['level'] == 'Advanced'
```