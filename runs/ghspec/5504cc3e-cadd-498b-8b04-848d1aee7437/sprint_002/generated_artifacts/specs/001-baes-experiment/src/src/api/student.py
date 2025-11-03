```python
from flask import Blueprint, request, jsonify
from src.models.student import Student, StudentError  # Assuming Student model is in this path
from flask_sqlalchemy import SQLAlchemy
import re

# Create a blueprint for the student API
student_api = Blueprint('student_api', __name__)
db = SQLAlchemy()  # Assuming db is initialized correctly

# Regular expression for validating email addresses
EMAIL_REGEX = r"(^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$)"

def validate_email(email):
    """
    Validate the format of the provided email address.

    Args:
        email (str): The email address to validate.

    Raises:
        ValueError: If the email format is invalid.
    """
    if not re.match(EMAIL_REGEX, email):
        raise ValueError("Invalid email format.")

@student_api.route('/api/v1/students', methods=['POST'])
def create_student():
    """
    Create a new student with a name and email.

    Request Payload:
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }

    Returns:
        JSON response indicating success or failure.
    """
    data = request.json
    name = data.get('name')
    email = data.get('email')

    try:
        validate_email(email)
        new_student = Student(name=name, email=email)
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student created successfully"}), 201

    except (ValueError, StudentError) as e:
        return jsonify({"error": {"code": "E001", "message": str(e)}}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Unable to create student"}}), 500

@student_api.route('/api/v1/students', methods=['GET'])
def get_students():
    """
    Retrieve a list of all registered students with their email addresses.

    Returns:
        JSON response with list of students.
    """
    students = Student.query.all()
    return jsonify({"data": [{"id": student.id, "name": student.name, "email": student.email} for student in students]}), 200

@student_api.route('/api/v1/students/<int:id>', methods=['PUT'])
def update_student_email(id):
    """
    Update an existing student's email address.

    Request Payload:
    {
      "email": "jane.doe@example.com"
    }

    Returns:
        JSON response indicating success or failure.
    """
    data = request.json
    email = data.get('email')

    try:
        validate_email(email)
        student = Student.query.get_or_404(id)
        student.email = email
        db.session.commit()
        return jsonify({"message": "Student email updated successfully"}), 200

    except (ValueError, StudentError) as e:
        return jsonify({"error": {"code": "E001", "message": str(e)}}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Unable to update student email"}}), 500
```