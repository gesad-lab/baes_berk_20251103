```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)  # Added email field

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a student record
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data.get('name') or not data.get('email'):
        return jsonify({"error": {"code": "E002", "message": "Name and email are required."}}), 400
    # In a real scenario, we would validate email format here
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student created successfully."}), 201

# API endpoint to retrieve student records
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"name": student.name, "email": student.email} for student in students]), 200

# Test Cases
def test_create_student_with_email():
    response = app.test_client().post('/students', json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert b'Student created successfully.' in response.data

def test_create_student_missing_email():
    response = app.test_client().post('/students', json={"name": "John Doe"})
    assert response.status_code == 400
    assert b'Name and email are required.' in response.data

def test_get_students():
    app.test_client().post('/students', json={"name": "John Doe", "email": "john@example.com"})
    response = app.test_client().get('/students')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['name'] == "John Doe"
    assert data[0]['email'] == "john@example.com"
```