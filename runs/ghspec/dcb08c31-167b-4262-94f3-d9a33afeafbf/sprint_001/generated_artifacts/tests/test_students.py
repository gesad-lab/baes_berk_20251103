```python
import json
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name: str):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

# API endpoint to add a student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name cannot be empty"}}), 400

    new_student = Student(name=name)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"id": new_student.id, "name": new_student.name}), 201

# API endpoint to retrieve all students
@app.route('/students', methods=['GET'])
def retrieve_students():
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

# Create the database schema before tests
@app.before_first_request
def create_tables():
    db.create_all()

# Tests for the student API
@pytest.fixture
def client():
    with app.test_client() as testing_client:
        yield testing_client

def test_retrieve_students_empty(client):
    """Test retrieving students when no students exist."""
    response = client.get('/students')
    assert response.status_code == 200
    assert response.json == []

def test_add_student(client):
    """Test adding a new student."""
    response = client.post('/students', json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json['name'] == "John Doe"

def test_retrieve_students_after_addition(client):
    """Test retrieving students after adding a student."""
    client.post('/students', json={"name": "John Doe"})
    response = client.get('/students')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == "John Doe"

def test_add_student_with_empty_name(client):
    """Test adding a student with an empty name."""
    response = client.post('/students', json={"name": ""})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E001", "message": "Name cannot be empty"}}
```