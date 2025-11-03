import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({'error': {'code': 'E001', 'message': 'Missing required field: name'}}), 400

    student = Student(name=name)
    db.session.add(student)
    db.session.commit()
    
    return jsonify({'id': student.id, 'name': student.name}), 201

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404

    return jsonify({'name': student.name}), 200

# Unit tests for student creation
def test_create_student_success(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert response.json == {'id': 1, 'name': 'John Doe'}

def test_create_student_missing_name(client):
    response = client.post('/students', json={})
    assert response.status_code == 400
    assert response.json == {'error': {'code': 'E001', 'message': 'Missing required field: name'}}

def test_get_student_success(client):
    # First create a student
    create_response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = create_response.json['id']
    
    # Now retrieve the student by ID
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json == {'name': 'Jane Doe'}

def test_get_student_not_found(client):
    response = client.get('/students/999')
    assert response.status_code == 404
    assert response.json == {'error': {'code': 'E002', 'message': 'Student not found'}}

@pytest.fixture
def client():
    with app.test_client() as client:
        db.create_all()  # Create the database schema
        yield client
        db.drop_all()  # Clean up after tests

def test_api(client):
    test_create_student_success(client)
    test_create_student_missing_name(client)
    test_get_student_success(client)
    test_get_student_not_found(client)