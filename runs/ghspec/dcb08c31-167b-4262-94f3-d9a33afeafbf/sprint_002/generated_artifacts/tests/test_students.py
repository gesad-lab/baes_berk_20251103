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
    email = db.Column(db.String, nullable=False)  # New email field added, required

# Create the database tables
with app.app_context():
    db.create_all()

# Sample POST endpoint to create a student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    
    # Validate input
    if 'name' not in data or 'email' not in data:
        return jsonify({"error": {"code": "E001", "message": "Both name and email are required."}}), 400

    # Create a new student
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201

# Sample GET endpoint to retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    # Constructs a list of student details including email
    return jsonify([{"id": student.id, "name": student.name, "email": student.email} for student in students])

# Tests
def test_create_and_get_students():
    with app.test_request_context():
        # Test POST request to create a new student
        response = app.test_client().post('/students', json={"name": "John Doe", "email": "john.doe@example.com"})
        assert response.status_code == 201
        assert response.json['name'] == 'John Doe'
        assert response.json['email'] == 'john.doe@example.com'

        # Test GET request to retrieve students
        response = app.test_client().get('/students')
        assert response.status_code == 200
        data = response.json
        assert len(data) == 1
        assert data[0]['name'] == 'John Doe'
        assert data[0]['email'] == 'john.doe@example.com'
```