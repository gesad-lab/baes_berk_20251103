```
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
    email = db.Column(db.String, nullable=False)  # Added email field

# Create Student API Endpoint
@app.route('/students', methods=['POST'])
def create_student():
    """Creates a new student record."""
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    # Validate input
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email fields are required"}}), 400
    
    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Retrieve a student record by ID."""
    student = Student.query.get(id)
    
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
    
    return jsonify({"id": student.id, "name": student.name, "email": student.email}), 200

@app.route('/students', methods=['GET'])
def list_students():
    """List all student records."""
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name, "email": student.email} for student in students]), 200

# Initialize the database
with app.app_context():
    db.create_all()
```