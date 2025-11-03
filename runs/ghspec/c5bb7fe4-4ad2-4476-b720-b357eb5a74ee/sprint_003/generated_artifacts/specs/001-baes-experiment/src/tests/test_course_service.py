```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.models import Course  # Import the new Course model
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and db for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create all database tables for testing
with app.app_context():
    db.create_all()

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new Course."""
    data = request.get_json()
    
    # Validate input
    if not data or not all(key in data for key in ('name', 'level')):
        return jsonify({"error": {"code": "E001", "message": "Invalid input. 'name' and 'level' are required."}}), 400
    
    course = Course(name=data['name'], level=data['level'])
    db.session.add(course)
    db.session.commit()
    
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 201

@app.route('/courses', methods=['GET'])
def get_all_courses():
    """Retrieve all Courses."""
    courses = Course.query.all()
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses]), 200

@app.route('/courses/<int:id>', methods=['PUT'])
def update_course_level(id):
    """Update the level of an existing Course."""
    data = request.get_json()
    
    # Validate input
    if not data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Invalid input. 'level' is required."}}), 400
    
    course = Course.query.get(id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404
    
    course.level = data['level']
    db.session.commit()
    
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200

# Tests for Course API
@pytest.mark.parametrize("data, expected_status", [
    ({"name": "Math 101", "level": "Beginner"}, 201),
    ({"name": "Science 101"}, 400),  # Missing level
    ({"level": "Intermediate"}, 400),  # Missing name
])
def test_create_course(data, expected_status):
    """Test course creation with various input."""
    response = app.test_client().post('/courses', json=data)
    assert response.status_code == expected_status

def test_get_all_courses():
    """Test retrieval of all courses."""
    app.test_client().post('/courses', json={"name": "Math 101", "level": "Beginner"})
    response = app.test_client().get('/courses')
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_update_course_level():
    """Test updating course level."""
    response = app.test_client().post('/courses', json={"name": "Math 101", "level": "Beginner"})
    course_id = response.get_json()['id']
    update_response = app.test_client().put(f'/courses/{course_id}', json={"level": "Intermediate"})
    
    assert update_response.status_code == 200
    assert update_response.get_json()['level'] == "Intermediate"
```