```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Assuming the app and db have been initialized in your main application code
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Assuming a Course model is defined in models.py
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    level = db.Column(db.String(50), nullable=False)

# Sample API endpoint to create a course
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data or 'name' not in data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Invalid input, 'name' and 'level' are required."}}), 400
    
    new_course = Course(name=data['name'], level=data['level'])
    db.session.add(new_course)
    db.session.commit()
    
    return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201

# Sample API endpoint to retrieve all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses]), 200

# Test cases for course creation and retrieval
def test_create_course(client):
    response = client.post('/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['name'] == 'Mathematics'
    assert response.json['level'] == 'Beginner'

def test_create_course_invalid(client):
    response = client.post('/courses', json={'name': '', 'level': ''})
    assert response.status_code == 400
    assert response.json == {
        "error": {
            "code": "E001",
            "message": "Invalid input, 'name' and 'level' are required."
        }
    }

def test_get_courses(client):
    client.post('/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    response = client.get('/courses')
    assert response.status_code == 200
    assert len(response.json) > 0

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables
            yield client
        db.drop_all()  # Drop tables after tests

# You can run the following command to check the coverage:
# pytest --cov=src tests/
```