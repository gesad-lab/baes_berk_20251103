```python
from flask import Flask, jsonify, request
from api.models import Student
from api import db
import re

app = Flask(__name__)

# Helper function to validate email format
def is_valid_email(email: str) -> bool:
    """Validate the email format using regular expressions."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/students/', methods=['POST'])
def create_student():
    """Create a new student with required name and email fields."""
    data = request.get_json()

    # Validate name
    if 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Missing name field."}}), 400
    
    # Validate email
    if 'email' not in data or not data['email']:
        return jsonify({"error": {"code": "E002", "message": "Missing email field."}}), 400
    if not is_valid_email(data['email']):
        return jsonify({"error": {"code": "E003", "message": "Invalid email format."}}), 400

    # Create new student record
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201

@app.route('/students/', methods=['GET'])
def get_students():
    """Retrieve all registered students."""
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name, "email": student.email} for student in students]), 200

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id: int):
    """Retrieve a specific student by ID."""
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": {"code": "E004", "message": "Student not found."}}), 404
    
    return jsonify({"id": student.id, "name": student.name, "email": student.email}), 200
```