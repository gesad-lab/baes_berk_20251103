# File: src/controllers/student_controller.py

"""
Student Controller manages the API endpoints for student operations.
This includes adding a student with an email, retrieving all students,
and handling necessary validations and error responses.
"""

from flask import Blueprint, request, jsonify
from models.student import Student
from database import db
from schemas.student_schema import StudentSchema
from sqlalchemy.exc import IntegrityError

student_api = Blueprint('student_api', __name__)

@student_api.route('/students', methods=['POST'])
def add_student():
    """
    Adds a new student with a name and email address.

    Request Body:
    - name (str): Name of the student (required)
    - email (str): Email of the student (required)

    Returns:
    - 201 Created with student details on success.
    - 400 Bad Request on validation errors.
    """
    json_data = request.get_json()
    schema = StudentSchema()
    try:
        # Validate and deserialize input
        student_data = schema.load(json_data)
        
        # Create a new student instance
        new_student = Student(name=student_data['name'], email=student_data['email'])

        # Persist the new student to the database
        db.session.add(new_student)
        db.session.commit()

        # Serialize the new student object
        result = schema.dump(new_student)
        return jsonify(result), 201  # Successfully created

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E001", "message": "Email already exists."}}), 400
        
    except Exception as e:
        # Catch all other exceptions and return a generic error
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 400

@student_api.route('/students', methods=['GET'])
def get_students():
    """
    Retrieves a list of all students with their names and emails.

    Returns:
    - 200 OK with a list of students in JSON format.
    """
    # Fetch all student records
    students = Student.query.all()
    
    # Serialize the students data
    schema = StudentSchema(many=True)
    result = schema.dump(students)

    return jsonify(result), 200  # Successfully fetched

# Error Handling for Missing Email
def validate_student_data(data):
    """
    Validate the presence of name and email in the provided data.
    
    Args:
        data (dict): The student data to validate.
    
    Raises:
        ValueError: If name or email is missing.
    """
    if 'name' not in data or 'email' not in data:
        raise ValueError("Both name and email are required.")

# Example Usage:
# When adding a student, the request body can be as follows:
# {
#     "name": "John Doe",
#     "email": "john.doe@example.com"
# }
# Expected successful response:
# HTTP 201 Created
# {
#     "name": "John Doe",
#     "email": "john.doe@example.com"
# }

# When retrieving all students, the response will look like:
# HTTP 200 OK
# [
#     {
#         "name": "John Doe",
#         "email": "john.doe@example.com"
#     },
#     {
#         "name": "Jane Smith",
#         "email": "jane.smith@example.com"
#     }
# ]
