```python
from flask import Blueprint, jsonify, request
from src.models import Student
from src.services.student_service import create_student, get_students, update_student
from sqlalchemy.exc import IntegrityError

# Define a Blueprint for the student API
student_api = Blueprint('student_api', __name__)

@student_api.route('/students', methods=['POST'])
def create_student_endpoint():
    """Create a new student with a name and email.

    Args:
        name (str): The name of the student.
        email (str): The email address of the student (required).

    Returns:
        Response: JSON representation of the created student, including the email, and HTTP status 201.
    """
    data = request.json
    try:
        student = create_student(data['name'], data['email'])  # Pass name and email to the service
        return jsonify(student), 201
    except KeyError as e:
        return jsonify({"error": {"code": "E001", "message": f"Missing required field: {str(e)}"}}), 400
    except IntegrityError:
        return jsonify({"error": {"code": "E002", "message": "Email already exists."}}), 400
    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": "Failed to create student.", "details": str(e)}}), 500

@student_api.route('/students', methods=['GET'])
def retrieve_students_endpoint():
    """Retrieve all students.

    Returns:
        Response: JSON array of student objects, each including their email, and HTTP status 200.
    """
    students = get_students()
    return jsonify(students), 200

@student_api.route('/students/<int:id>', methods=['PUT'])
def update_student_email_endpoint(id):
    """Update the email of an existing student.

    Args:
        id (int): The ID of the student to update.
        email (str): The new email address of the student (required).

    Returns:
        Response: JSON representation of the updated student including the email, and HTTP status 200.
    """
    data = request.json
    try:
        updated_student = update_student(id, data['email'])  # Pass student ID and new email to the service
        return jsonify(updated_student), 200
    except KeyError as e:
        return jsonify({"error": {"code": "E001", "message": f"Missing required field: {str(e)}"}}), 400
    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": "Failed to update student email.", "details": str(e)}}), 500
```