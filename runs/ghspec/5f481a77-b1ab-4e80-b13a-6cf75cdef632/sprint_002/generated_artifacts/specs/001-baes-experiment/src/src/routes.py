from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError, validate
from .models import Student, db

routes = Blueprint('routes', __name__)

class StudentSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)  # Email field with validation

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@routes.route('/students', methods=['POST'])
def create_student():
    """Create a new student with name and email."""
    try:
        # Validate and deserialize input
        student_data = student_schema.load(request.json)
        
        # Create new student instance
        new_student = Student(name=student_data['name'], email=student_data['email'])
        db.session.add(new_student)
        db.session.commit()
        
        return jsonify(student_schema.dump(new_student)), 201
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Validation error", "details": err.messages}}), 400
    except Exception as e:
        # Log error details for debugging (avoid logging sensitive information)
        return jsonify({"error": {"code": "E002", "message": "Could not create the student", "details": str(e)}}), 500

@routes.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Fetch a student's details by ID."""
    student = Student.query.get(student_id)
    if student is None:
        return jsonify({"error": {"code": "E003", "message": "Student not found"}}), 404
    
    return jsonify(student_schema.dump(student)), 200

# Additional routes and logic can be added below
