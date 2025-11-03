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
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)  # Add email field

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve a list of all students with their names and emails."""
    students = Student.query.all()
    return jsonify([{"name": student.name, "email": student.email} for student in students]), 200

# API endpoint to create a student record
@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student record with name and email."""
    data = request.get_json()
    
    if not data or 'name' not in data or not isinstance(data['name'], str):
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Name field is required and must be a string."
            }
        }), 400
    
    if 'email' not in data or not isinstance(data['email'], str) or not is_valid_email(data['email']):
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Email field is required and must be a valid email format."
            }
        }), 400
    
    student = Student(name=data['name'], email=data['email'])
    db.session.add(student)
    db.session.commit()
    
    return jsonify({"message": "Student created successfully."}), 201

def is_valid_email(email: str) -> bool:
    """Check if the given email is valid by using a simple regex pattern."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None
```