```python
# src/api/student_api.py

from flask import Blueprint, request, jsonify
from src.services.student_service import StudentService
import re

student_api = Blueprint('student_api', __name__)

def is_valid_email(email: str) -> bool:
    """
    Validate the email format using a regex pattern.

    Parameters:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

@student_api.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student record.

    Request Body:
    {
        "name": "Student Name",
        "email": "student@example.com"
    }

    Returns:
        JSON: Success message and student ID upon successful creation,
              or error message if validation fails.
    """
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')

    # Validate input
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email fields are required."}}), 400
    
    if not is_valid_email(email):
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    # Call the service to create the student
    student_service = StudentService()
    student_id = student_service.create_student(name, email)

    return jsonify({"message": "Student created successfully.", "student_id": student_id}), 201
```