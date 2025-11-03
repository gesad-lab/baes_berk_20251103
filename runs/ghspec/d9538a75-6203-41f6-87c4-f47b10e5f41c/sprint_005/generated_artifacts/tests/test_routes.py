```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Assuming the app and db have been initialized in your main application code
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Sample API endpoint to create a course
@app.route('/api/v1/students/<int:student_id>/courses', methods=['POST'])
def associate_course(student_id):
    data = request.json
    course_id = data.get('course_id')
    # Logic to associate course with student
    return jsonify({"message": "Course associated successfully"}), 200


# New API endpoint to create a teacher
@app.route('/api/v1/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Both name and email are required"}}), 400
    
    # Logic to check for existing teacher email should go here

    # Logic to create and store a new teacher should go here

    return jsonify({"message": "Teacher created successfully"}), 201


# New API endpoint to retrieve a teacher
@app.route('/api/v1/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    # Logic to retrieve and return teacher details should go here
    return jsonify({"id": teacher_id, "name": "Example Name", "email": "example@example.com"})


# Test cases for the teacher functionality
def test_create_teacher(client):
    response = client.post('/api/v1/teachers', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 201
    assert response.json['message'] == "Teacher created successfully"

def test_create_teacher_missing_fields(client):
    response = client.post('/api/v1/teachers', json={'name': '', 'email': 'john.doe@example.com'})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"

def test_get_teacher(client):
    response = client.get('/api/v1/teachers/1')
    assert response.status_code == 200
    assert response.json['id'] == 1
    assert response.json['name'] == "Example Name"
    assert response.json['email'] == "example@example.com"

# Initialize the Flask testing client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
```