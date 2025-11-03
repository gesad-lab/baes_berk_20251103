```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import re

# Create a Flask application for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Create Student Endpoint
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    # Validate input
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400
    if not is_valid_email(email):
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201

def is_valid_email(email):
    # Simple email validation regex
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Tests for Student Creation
def test_create_student_with_valid_email(client):
    response = client.post('/students', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json['name'] == "John Doe"
    assert response.json['email'] == "john.doe@example.com"

def test_create_student_without_email(client):
    response = client.post('/students', json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json['error']['message'] == "Name and email are required."

def test_create_student_with_invalid_email(client):
    response = client.post('/students', json={"name": "John Doe", "email": "not-an-email"})
    assert response.status_code == 400
    assert response.json['error']['message'] == "Invalid email format."

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
```