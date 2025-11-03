from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, validate, ValidationError
from models import Student, db

# Define a blueprint for the student routes
student_bp = Blueprint('students', __name__)

class StudentSchema(Schema):
    """Schema for validating student registration data."""
    name = fields.Str(required=True)
    email = fields.Str(required=True, validate=validate.Email())
    
# Initialize the schema
student_schema = StudentSchema()

@student_bp.route('/students', methods=['POST'])
def create_student():
    """Endpoint to create a new student."""
    try:
        # Validate incoming data
        student_data = student_schema.load(request.json)

        # Create a new student instance
        new_student = Student(**student_data)

        # Add to the database
        db.session.add(new_student)
        db.session.commit()

        return jsonify({
            'id': new_student.id,
            'name': new_student.name,
            'email': new_student.email
        }), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({
            'error': {
                'code': 'E002',
                'message': 'Email is required.'
            }
        }), 400
    except Exception as e:
        # Log the exception for debugging
        db.session.rollback()  # Rollback the session on error
        return jsonify({
            'error': {
                'code': 'E003',
                'message': 'An unexpected error occurred.'
            }
        }), 500

@student_bp.route('/students', methods=['GET'])
def get_students():
    """Endpoint to retrieve the list of all registered students."""
    students = Student.query.all()
    # Serialize the student data
    return jsonify([{
        'id': student.id,
        'name': student.name,
        'email': student.email
    } for student in students]), 200

# Register the blueprint in the main app (presumably done in app.py)
# app.register_blueprint(student_bp)