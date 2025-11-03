import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Create Student API Endpoint
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': {'code': 'E001', 'message': 'Name is required'}}), 400

    student = Student(name=name)
    db.session.add(student)
    db.session.commit()
    return jsonify({'id': student.id, 'name': student.name}), 201

# Get Student API Endpoint
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404
    return jsonify({'id': student.id, 'name': student.name})

# List Students API Endpoint
@app.route('/students', methods=['GET'])
def list_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students])

@pytest.fixture
def client():
    # Setup in-memory database and create tables
    db.create_all()
    yield app.test_client()
    db.session.remove()
    db.drop_all()

def test_create_student(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['name'] == 'John Doe'

def test_create_student_missing_name(client):
    response = client.post('/students', json={})
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E001'
    assert response.json['error']['message'] == 'Name is required'

def test_get_student(client):
    # First create a student to retrieve
    response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = response.json['id']

    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json['id'] == student_id
    assert response.json['name'] == 'Jane Doe'

def test_get_non_existent_student(client):
    response = client.get('/students/999')
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E002'
    assert response.json['error']['message'] == 'Student not found'

def test_list_students_empty(client):
    response = client.get('/students')
    assert response.status_code == 200
    assert response.json == []

def test_list_students_with_data(client):
    client.post('/students', json={'name': 'Student One'})
    client.post('/students', json={'name': 'Student Two'})
    
    response = client.get('/students')
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['name'] in ['Student One', 'Student Two']
    assert response.json[1]['name'] in ['Student One', 'Student Two']