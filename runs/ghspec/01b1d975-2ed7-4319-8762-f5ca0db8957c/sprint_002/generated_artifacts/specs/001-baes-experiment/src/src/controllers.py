```python
# File: src/routes.py

from flask import Blueprint, request, jsonify
from src.controllers import add_student, get_students
from src.validation import validate_student_email

# Define a Blueprint for the student routes
student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['POST'])
def create_student():
    """API endpoint to add a new student with email."""
    data = request.get_json()

    # Validate and extract student data from request
    if 'name' not in data or 'email' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400

    # Validate email format
    email_validation_result = validate_student_email(data['email'])
    if email_validation_result:
        return jsonify({"error": {"code": "E002", "message": email_validation_result}}), 400

    # Call the controller to add the student
    student = add_student(data['name'], data['email'])
    
    # Return the created student data
    return jsonify({"id": student.id, "name": student.name, "email": student.email}), 201

@student_bp.route('/students', methods=['GET'])
def list_students():
    """API endpoint to retrieve all students."""
    students = get_students()

    # Format student data for response
    student_list = [{"id": student.id, "name": student.name, "email": student.email} for student in students]
    
    return jsonify(student_list), 200
```