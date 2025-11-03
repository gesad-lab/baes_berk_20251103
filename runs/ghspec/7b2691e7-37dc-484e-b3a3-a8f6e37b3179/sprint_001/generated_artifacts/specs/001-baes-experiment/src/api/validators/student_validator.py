```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from .models import Student  # Assuming the Student model is in your models.py
from .extensions import db  # Assuming you use SQLAlchemy for database interaction

# Create a blueprint for the student API
student_bp = Blueprint('student', __name__)

class StudentSchema(Schema):
    """Schema to validate student data."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, error_messages={"required": "Name is required."})

@student_bp.route('/students', methods=['GET'])
def retrieve_student():
    """Retrieve a student by ID.
    
    Returns a JSON response with the student's name if found, 
    or a 404 error if not found.
    """
    student_id = request.args.get('id')
    
    if not student_id:
        return jsonify({"error": {"code": "E001", "message": "Missing 'id' query parameter."}}), 400
    
    student = Student.query.get(student_id)
    
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404
    
    return jsonify({"name": student.name}), 200

@student_bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student and return the created student data."""
    schema = StudentSchema()
    
    try:
        # Validate and load request data
        student_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    
    # Create a new student record
    new_student = Student(**student_data)
    
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify(schema.dump(new_student)), 201
```