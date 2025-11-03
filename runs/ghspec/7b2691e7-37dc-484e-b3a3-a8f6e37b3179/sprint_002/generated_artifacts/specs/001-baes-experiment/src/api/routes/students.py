```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError, validate
from models import Student, db  # Assuming these are defined in models.py
from sqlalchemy.exc import IntegrityError
import re

students_bp = Blueprint('students', __name__)

class StudentSchema(Schema):
    """Schema to validate student data, including a valid email format."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True, validate=validate.Email())

@students_bp.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student record.

    Request example:
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    
    Returns:
    - 201 Created with student details on success
    - 400 Bad Request if 'name' or 'email' is missing or invalid
    """
    schema = StudentSchema()
    try:
        # Validate and deserialize input
        student_data = schema.load(request.json)
    except ValidationError as err:
        # Return error response for invalid data
        return jsonify({"error": {"code": "E001", "message": "Invalid email format"}}), 400
    
    # Instantiate a new Student object
    new_student = Student(name=student_data['name'], email=student_data['email'])
    
    try:
        # Add to the database
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201
    except IntegrityError:
        # Rollback session in case of a failure
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Student already exists"}}, 400)

@students_bp.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """
    Retrieve a student record by its identifier.

    Returns:
    - 200 OK with the student's details if found
    - 404 Not Found if the student does not exist
    """
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
    
    return jsonify({"id": student.id, "name": student.name, "email": student.email}), 200
```