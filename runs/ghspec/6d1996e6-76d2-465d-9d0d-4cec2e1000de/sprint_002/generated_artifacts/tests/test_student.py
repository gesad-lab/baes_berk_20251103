```python
# src/services/student.py

from models.student import Student
from db.database import db_session
from utils.email_validators import is_valid_email
from flask import jsonify, request, abort

def create_student():
    """
    Create a new student record.

    :return: JSON response with student details or error message
    """
    data = request.get_json()
    
    # Extract name and email from the request data
    name = data.get("name")
    email = data.get("email")

    # Validate name and email
    if not name or not email:
        abort(400, {"error": {"code": "E001", "message": "Name and email are required."}})
    if not is_valid_email(email):
        abort(400, {"error": {"code": "E002", "message": "Invalid email format."}})

    # Create a new Student object
    new_student = Student(name=name, email=email)
    db_session.add(new_student)
    db_session.commit()
    
    # Return a success response
    return jsonify({"name": new_student.name, "email": new_student.email}), 201

def update_student_email(student_id):
    """
    Update the email address for an existing student.

    :param student_id: ID of the student to update
    :return: JSON response confirming the update or error message
    """
    data = request.get_json()
    new_email = data.get("email")
    
    # Validate new email
    if not new_email:
        abort(400, {"error": {"code": "E001", "message": "Email is required."}})
    if not is_valid_email(new_email):
        abort(400, {"error": {"code": "E002", "message": "Invalid email format."}})

    # Retrieve the student object
    student = db_session.query(Student).get(student_id)
    if not student:
        abort(404, {"error": {"code": "E003", "message": "Student not found."}})

    # Update email and commit to database
    student.email = new_email
    db_session.commit()

    # Return a success response
    return jsonify({"message": "Email updated successfully.", "email": student.email}), 200

def get_student(student_id):
    """
    Retrieve a student's information by ID.

    :param student_id: ID of the student to retrieve
    :return: JSON response with student information
    """
    student = db_session.query(Student).get(student_id)
    if not student:
        abort(404, {"error": {"code": "E003", "message": "Student not found."}})

    return jsonify({"name": student.name, "email": student.email}), 200
```