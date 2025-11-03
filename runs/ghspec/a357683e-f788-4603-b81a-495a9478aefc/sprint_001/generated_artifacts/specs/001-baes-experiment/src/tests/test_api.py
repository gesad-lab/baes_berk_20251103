import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Setup Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    # Validate input data
    if 'name' not in data or 'age' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Invalid input format'}}), 400

    student = Student(name=data['name'], age=data['age'])
    db.session.add(student)
    db.session.commit()
    return jsonify({'id': student.id}), 201

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{ 'id': student.id, 'name': student.name, 'age': student.age } for student in students]), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if student is None:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404
    return jsonify({'id': student.id, 'name': student.name, 'age': student.age}), 200

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if student is None:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404

    data = request.get_json()
    if 'name' in data:
        student.name = data['name']
    if 'age' in data:
        student.age = data['age']

    db.session.commit()
    return jsonify({'id': student.id, 'name': student.name, 'age': student.age}), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if student is None:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404

    db.session.delete(student)
    db.session.commit()
    return '', 204

# Unit tests for API endpoints
def test_create_student(client):
    response = client.post('/students', json={'name': 'Alice', 'age': 20})
    assert response.status_code == 201
    assert 'id' in response.get_json()

def test_create_student_invalid_input(client):
    response = client.post('/students', json={'name': 'Alice'})
    assert response.status_code == 400
    assert response.get_json() == {'error': {'code': 'E001', 'message': 'Invalid input format'}}

def test_get_students(client):
    client.post('/students', json={'name': 'Alice', 'age': 20})
    response = client.get('/students')
    assert response.status_code == 200
    students = response.get_json()
    assert len(students) == 1
    assert students[0]['name'] == 'Alice'

def test_get_student(client):
    client.post('/students', json={'name': 'Bob', 'age': 22})
    response = client.get('/students/1')  # Assuming it will be created with ID 1
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Bob'

def test_get_student_not_found(client):
    response = client.get('/students/999')
    assert response.status_code == 404
    assert response.get_json() == {'error': {'code': 'E002', 'message': 'Student not found'}}

def test_update_student(client):
    client.post('/students', json={'name': 'Charlie', 'age': 21})
    response = client.put('/students/1', json={'age': 22})
    assert response.status_code == 200
    assert response.get_json()['age'] == 22

def test_update_student_not_found(client):
    response = client.put('/students/999', json={'age': 22})
    assert response.status_code == 404
    assert response.get_json() == {'error': {'code': 'E002', 'message': 'Student not found'}}

def test_delete_student(client):
    client.post('/students', json={'name': 'Dave', 'age': 23})
    response = client.delete('/students/1')
    assert response.status_code == 204
    assert client.get('/students/1').status_code == 404

def test_delete_student_not_found(client):
    response = client.delete('/students/999')
    assert response.status_code == 404
    assert response.get_json() == {'error': {'code': 'E002', 'message': 'Student not found'}}