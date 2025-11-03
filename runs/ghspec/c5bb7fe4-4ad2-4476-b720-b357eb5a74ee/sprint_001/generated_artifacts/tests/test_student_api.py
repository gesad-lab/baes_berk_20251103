import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and db for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create all database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoints
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Name is required'}}), 400
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'id': new_student.id, 'name': new_student.name}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404
    return jsonify({'id': student.id, 'name': student.name}), 200

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404
    data = request.get_json()
    student.name = data['name']
    db.session.commit()
    return jsonify({'id': student.id, 'name': student.name}), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'}), 204

# Integration tests for API endpoints
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_student(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    json_data = response.get_json()
    assert 'id' in json_data
    assert json_data['name'] == 'John Doe'

def test_get_student(client):
    response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = response.get_json()['id']
    
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['id'] == student_id
    assert json_data['name'] == 'Jane Doe'

def test_update_student(client):
    response = client.post('/students', json={'name': 'Jake Doe'})
    student_id = response.get_json()['id']
    
    response = client.put(f'/students/{student_id}', json={'name': 'Jake Smith'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['name'] == 'Jake Smith'

def test_delete_student(client):
    response = client.post('/students', json={'name': 'Jim Doe'})
    student_id = response.get_json()['id']
    
    response = client.delete(f'/students/{student_id}')
    assert response.status_code == 204
    
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 404  # Student should no longer exist

def test_create_student_without_name(client):
    response = client.post('/students', json={})
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error']['code'] == 'E001'

def test_get_nonexistent_student(client):
    response = client.get('/students/999')
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data['error']['code'] == 'E002'