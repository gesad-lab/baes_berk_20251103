```python
import json
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database schema
@app.before_first_request
def create_tables():
    db.create_all()

# Define the API endpoint for retrieving students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students])

# Define the API endpoint for creating students
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    if not data.get('name'):
        return jsonify({'error': 'E001: Name is required'}), 400
    
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'id': new_student.id, 'message': 'Student created successfully'}), 201

# Unit tests for the API
@pytest.mark.parametrize("name, expected_status_code", [
    ("John Doe", 201),
    ("", 400)  # Invalid name should return error
])
def test_student_creation(name, expected_status_code):
    response = app.test_client().post('/students', json={'name': name})
    assert response.status_code == expected_status_code

def test_get_students_empty():
    response = app.test_client().get('/students')
    assert response.json == []
    assert response.status_code == 200

def test_student_creation_success():
    response = app.test_client().post('/students', json={'name': 'Jane Doe'})
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['message'] == 'Student created successfully'

def test_student_retrieval():
    # Create a student to test retrieval
    app.test_client().post('/students', json={'name': 'John Smith'})
    response = app.test_client().get('/students')
    assert response.status_code == 200
    student_names = [student['name'] for student in response.json]
    assert 'John Smith' in student_names
```