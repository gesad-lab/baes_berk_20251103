```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from src.models import Student
from src.database import db

# Create a blueprint for the API routes
api_bp = Blueprint('api', __name__)

# Schema for input validation using Marshmallow
class StudentSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "Name is required."})
    email = fields.Str(required=True, error_messages={"required": "Email is required."})

    @staticmethod
    def validate_email(email):
        # Simple regex for validating email formats
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValidationError("Invalid email format.")

# Route for creating a new student
@api_bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student with a name and email."""
    schema = StudentSchema()
    try:
        # Validate and deserialize input data
        data = schema.load(request.json)
        # Validate email format
        schema.validate_email(data['email'])

        # Create a new Student instance
        new_student = Student(name=data['name'], email=data['email'])
        db.session.add(new_student)
        db.session.commit()

        # Return the created student information
        return jsonify({
            'id': new_student.id,
            'name': new_student.name,
            'email': new_student.email
        }), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({'error': {'code': 'E001', 'message': str(err)}}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': {'code': 'E002', 'message': 'An unexpected error occurred.', 'details': str(e)}}), 500

# Route for updating an existing student
@api_bp.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    """Update an existing student's details."""
    schema = StudentSchema()
    try:
        # Validate and deserialize input data
        data = schema.load(request.json)
        # Validate email format
        schema.validate_email(data['email'])

        student = Student.query.get_or_404(id)
        student.name = data['name']
        student.email = data['email']
        db.session.commit()

        return jsonify({
            'id': student.id,
            'name': student.name,
            'email': student.email
        }), 200

    except ValidationError as err:
        return jsonify({'error': {'code': 'E001', 'message': str(err)}}), 400
    except Exception as e:
        return jsonify({'error': {'code': 'E002', 'message': 'An unexpected error occurred.', 'details': str(e)}}), 500

# Route for retrieving a specific student
@api_bp.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """Retrieve a student's details."""
    student = Student.query.get_or_404(id)
    return jsonify({
        'id': student.id,
        'name': student.name,
        'email': student.email
    }), 200
```