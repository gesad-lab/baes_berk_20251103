import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Assuming the app and db have been initialized in your main application code
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Assuming a Student model is defined in models.py
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)

# Sample API endpoint to create a student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    if 'email' not in data or not data['email']:
        return jsonify({'error': {'code': 'E001', 'message': 'Email is required'}}), 400
        
    # Here we could add email validation logic
    student = Student(email=data['email'])
    db.session.add(student)
    db.session.commit()
    return jsonify({'id': student.id, 'email': student.email}), 201

# Sample API endpoint to retrieve students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'email': student.email} for student in students]), 200

# Unit tests for API
@pytest.fixture
def client():
    db.create_all()  # Create test database
    yield app.test_client()  # Provides a testing client
    db.drop_all()  # Clean up after tests

def test_create_student_success(client):
    response = client.post('/students', json={'email': 'test@example.com'})
    assert response.status_code == 201
    assert response.json['email'] == 'test@example.com'

def test_create_student_missing_email(client):
    response = client.post('/students', json={})
    assert response.status_code == 400
    assert response.json == {'error': {'code': 'E001', 'message': 'Email is required'}}

def test_create_student_empty_email(client):
    response = client.post('/students', json={'email': ''})
    assert response.status_code == 400
    assert response.json == {'error': {'code': 'E001', 'message': 'Email is required'}}

def test_get_students_empty(client):
    response = client.get('/students')
    assert response.status_code == 200
    assert response.json == []

def test_get_students_success(client):
    client.post('/students', json={'email': 'test1@example.com'})
    client.post('/students', json={'email': 'test2@example.com'})
    response = client.get('/students')
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['email'] in ['test1@example.com', 'test2@example.com']
    assert response.json[1]['email'] in ['test1@example.com', 'test2@example.com']