import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

db.create_all()

# Mock CRUD operations
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E404", "message": "Student not found"}}), 404
    return jsonify({"id": student.id, "name": student.name}), 200

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E404", "message": "Student not found"}}), 404
    data = request.get_json()
    student.name = data['name']
    db.session.commit()
    return jsonify({"id": student.id, "name": student.name}), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E404", "message": "Student not found"}}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"}), 204


# Test file for student service functionalities
def test_create_student(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert response.json['name'] == 'John Doe'

def test_get_student(client):
    create_response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = create_response.json['id']
    
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Jane Doe'

def test_update_student(client):
    create_response = client.post('/students', json={'name': 'Mike Smith'})
    student_id = create_response.json['id']

    response = client.put(f'/students/{student_id}', json={'name': 'Michael Smith'})
    assert response.status_code == 200
    assert response.json['name'] == 'Michael Smith'

def test_delete_student(client):
    create_response = client.post('/students', json={'name': 'Lucy Brown'})
    student_id = create_response.json['id']

    response = client.delete(f'/students/{student_id}')
    assert response.status_code == 204

    response = client.get(f'/students/{student_id}')
    assert response.status_code == 404

def test_get_student_not_found(client):
    response = client.get('/students/9999')
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E404'
    assert response.json['error']['message'] == 'Student not found'