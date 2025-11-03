```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new course
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    # Validate required fields
    if 'name' not in data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name and level are required fields."}}), 400

    new_course = Course(name=data['name'], level=data['level'])
    db.session.add(new_course)
    db.session.commit()

    return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201

# Endpoint to get a specific course by ID
@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = Course.query.get(id)
    if course is None:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200

# Endpoint to list all courses
@app.route('/courses', methods=['GET'])
def list_courses():
    courses = Course.query.all()
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses]), 200

# Test cases for the Course entity
def test_create_course(client):
    response = client.post('/courses', json={'name': 'Math 101', 'level': 'Beginner'})
    assert response.status_code == 201
    assert response.get_json()['name'] == 'Math 101'

def test_create_course_without_name(client):
    response = client.post('/courses', json={'level': 'Beginner'})
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == 'E001'

def test_create_course_without_level(client):
    response = client.post('/courses', json={'name': 'Math 101'})
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == 'E001'

def test_get_course(client):
    client.post('/courses', json={'name': 'Math 101', 'level': 'Beginner'})
    response = client.get('/courses/1')
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Math 101'

def test_get_non_existent_course(client):
    response = client.get('/courses/999')
    assert response.status_code == 404
    assert response.get_json()['error']['code'] == 'E002'

def test_list_courses(client):
    client.post('/courses', json={'name': 'Math 101', 'level': 'Beginner'})
    client.post('/courses', json={'name': 'Science 101', 'level': 'Intermediate'})
    response = client.get('/courses')
    assert response.status_code == 200
    assert len(response.get_json()) == 2
```