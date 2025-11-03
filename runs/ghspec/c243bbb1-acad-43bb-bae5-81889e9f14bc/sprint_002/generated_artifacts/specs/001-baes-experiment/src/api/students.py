```python
# api/students.py

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
import re

students_bp = Blueprint('students', __name__)

# Regular expression for validating email format
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

@students_bp.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()

    # Validate presence of 'name' and 'email' fields
    name = data.get('name')
    email = data.get('email')

    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400

    if not email:
        return jsonify({"error": {"code": "E001", "message": "Email field is required."}}), 400

    if not re.match(EMAIL_REGEX, email):
        return jsonify({"error": {"code": "E002", "message": "Email field must be a valid email address."}}), 400

    # Assuming there's a function to save a student in the database
    try:
        # Placeholder code for saving student to the database
        student = save_student_to_db(name, email)  # This function should be defined in your data access layer

        return jsonify({
            "message": "Student created successfully",
            "student": {
                "id": student.id,
                "name": student.name,
                "email": student.email
            }
        }), 201

    except IntegrityError:
        return jsonify({"error": {"code": "E003", "message": "Student could not be created due to a database error."}}), 500

@students_bp.route('/students', methods=['GET'])
def get_students():
    # Assuming there's a function to retrieve all students from the database
    students = get_all_students_from_db()  # This function should be defined in your data access layer
    return jsonify([{
        "id": student.id,
        "name": student.name,
        "email": student.email
    } for student in students]), 200
```