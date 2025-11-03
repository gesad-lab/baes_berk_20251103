import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the tables in the database
with app.app_context():
    db.create_all()

# API Endpoint to create a new student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Name is required'}}), 400
    
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'id': new_student.id, 'name': new_student.name}), 201

# API Endpoint to retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200

# API Endpoint to update a student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404
    
    data = request.get_json()
    student.name = data.get('name', student.name)
    db.session.commit()
    return jsonify({'id': student.id, 'name': student.name}), 200

# API Endpoint to delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': {'code': 'E002', 'message': 'Student not found'}}), 404
    
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'}), 200

# Integration Tests for the API endpoints
def test_create_student(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert 'id' in response.json

def test_get_students(client):
    response = client.get('/students')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_update_student(client):
    response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = response.json['id']
    
    response = client.put(f'/students/{student_id}', json={'name': 'Jane Smith'})
    assert response.status_code == 200
    assert response.json['name'] == 'Jane Smith'

def test_delete_student(client):
    response = client.post('/students', json={'name': 'Alice'})
    student_id = response.json['id']
    
    response = client.delete(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Student deleted successfully'

def test_student_not_found(client):
    response = client.get('/students/999')
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E002'
    
# Fixture to initialize the test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Run the tests
if __name__ == '__main__':
    pytest.main()