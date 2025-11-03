```python
from flask import request, jsonify
from marshmallow import Schema, fields, ValidationError
from models import Student
from database import db

class StudentSchema(Schema):
    """Schema for validating student data."""
    name = fields.String(required=True)

student_schema = StudentSchema()

def create_student():
    """Create a new student in the database."""
    # Validate incoming request data against the schema
    try:
        data = student_schema.load(request.json)  # Validate input
    except ValidationError as err:
        # Return a well-defined error response for validation issues
        return jsonify({"error": {"code": "E001", "message": "Invalid data", "details": err.messages}}), 400

    # If validation passes, create a new student record
    student = Student(name=data['name'])
    
    # Add the student to the session and commit to the database
    db.session.add(student)
    db.session.commit()
    
    # Respond with the created student data
    return jsonify({"id": student.id, "name": student.name}), 201

def get_student(student_id):
    """Retrieve a student by ID."""
    student = Student.query.get(student_id)
    if student is None:
        # Return a 404 response if the student is not found
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
    
    # Return the student data
    return jsonify({"id": student.id, "name": student.name}), 200
```