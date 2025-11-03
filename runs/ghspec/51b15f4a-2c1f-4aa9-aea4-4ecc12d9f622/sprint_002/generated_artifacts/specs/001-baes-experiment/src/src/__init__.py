```python
# src/controllers/student_controller.py

from flask import Blueprint, request, jsonify
from models.student import Student
from app import db
import re

student_bp = Blueprint('student_bp', __name__)

def is_valid_email(email: str) -> bool:
    """Validate email format using a regex pattern."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

@student_bp.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    # Ensure both name and email are provided
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400
    if not email:
        return jsonify({"error": {"code": "E002", "message": "Email field is required."}}), 400
    if not is_valid_email(email):
        return jsonify({"error": {"code": "E003", "message": "Invalid email format."}}), 400

    # Create a new student and add to the database
    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201

@student_bp.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students with their email addresses."""
    students = Student.query.all()
    students_list = [{"id": student.id, "name": student.name, "email": student.email} for student in students]
    return jsonify(students_list), 200
```