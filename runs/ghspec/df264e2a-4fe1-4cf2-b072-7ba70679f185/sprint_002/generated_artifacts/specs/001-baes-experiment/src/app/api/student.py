```python
# app/api/student.py

from flask import Blueprint, request, jsonify
from app.models.student import Student  # Import the Student model
from app import db  # Import the database object
import re  # Regular expression module for email validation

student_bp = Blueprint('student', __name__)

def is_valid_email(email):
    # Validate the given email format using regex
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@student_bp.route('/students', methods=['POST'])
def create_student():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400
    if not is_valid_email(email):
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({"message": "Student created", "student": {"id": new_student.id, "name": new_student.name, "email": new_student.email}}), 201

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)  # Fetch student by ID

    if student is None:
        return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404

    response = {
        "id": student.id,
        "name": student.name,
        "email": student.email  # Include email in the response
    }
    return jsonify(response), 200
```