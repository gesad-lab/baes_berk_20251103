```python
import json
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application for the tests
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Route to add a student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Name is required"}}), 400

    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"id": new_student.id, "name": new_student.name}), 201

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

# Test cases
@pytest.fixture
def client():
    db.create_all()  # Create the database and tables
    yield app.test_client()
    db.drop_all()  # Clean up after tests

def test_add_student_valid(client):
    response = client.post('/students', json={"name": "John Doe"})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == "John Doe"

def test_get_students_empty(client):
    response = client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == []

def test_add_student_without_name(client):
    response = client.post('/students', json={})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == "E001"
    assert data['error']['message'] == "Name is required"

def test_add_student_retrieval(client):
    client.post('/students', json={"name": "Jane Smith"})
    response = client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['name'] == "Jane Smith"
```