```python
from flask import Blueprint, request, jsonify
import re
import logging

api_layer = Blueprint('api_layer', __name__)

# Configure structured logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_email(email):
    """Validate email format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@api_layer.route('/students', methods=['POST'])
def create_student():
    """Create a new student with name and email."""
    data = request.json
    name = data.get('name')
    email = data.get('email')

    # Validate input
    if not name or not email:
        logging.error('Failed to create student: Missing name or email')
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400

    if not validate_email(email):
        logging.error(f'Failed to create student: Invalid email format - {email}')
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    # Assuming you have a function `add_student_to_db` that interacts with your database.
    student_id = add_student_to_db(name, email)

    logging.info(f'Successfully created student: ID={student_id}, Name={name}, Email={email}')
    return jsonify({"id": student_id, "name": name, "email": email}), 201

@api_layer.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    """Update a student's name and/or email by ID."""
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if email and not validate_email(email):
        logging.error(f'Failed to update student with ID={id}: Invalid email format - {email}')
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    # Assuming you have a function `update_student_in_db` that interacts with your database.
    updated_student = update_student_in_db(id, name, email)

    if not updated_student:
        logging.error(f'Failed to update student: Student ID={id} not found.')
        return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404

    logging.info(f'Successfully updated student: ID={id}, Name={name}, Email={email}')
    return jsonify({"id": id, "name": name, "email": email}), 200

@api_layer.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Retrieve a student by ID."""
    student = get_student_from_db(id)  # Fetch student from database
    
    if not student:
        logging.error(f'Student not found: ID={id}')
        return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404

    logging.info(f'Retrieved student: ID={id}, Name={student["name"]}, Email={student["email"]}')
    return jsonify({"id": student["id"], "name": student["name"], "email": student["email"]}), 200
```