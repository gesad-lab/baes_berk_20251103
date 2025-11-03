from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from models import Teacher, db  # Importing the Teacher model
from sqlalchemy.exc import IntegrityError

teachers_bp = Blueprint('teachers', __name__)

class TeacherSchema(Schema):
    """Schema to validate teacher data, including a valid email format."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)

@teachers_bp.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new Teacher."""
    schema = TeacherSchema()
    try:
        # Load and validate input data
        data = schema.load(request.json)
        new_teacher = Teacher(name=data['name'], email=data['email'])
        
        # Attempt to add the new teacher to the database
        db.session.add(new_teacher)
        db.session.commit()
        
        # Return a success response with the created teacher's details
        return jsonify({"message": "Teacher created successfully.", "teacher": schema.dump(new_teacher)}), 201

    except ValidationError as err:
        # Return a validation error response with details
        return jsonify({"error": {"code": "E001", "message": "Validation errors occurred.", "details": err.messages}}), 400

    except IntegrityError:
        # Handle cases where the email already exists (unique constraint violation)
        db.session.rollback()  # Rollback the session to avoid inconsistencies
        return jsonify({"error": {"code": "E002", "message": "Email already exists."}}), 400

    except Exception as e:
        # Handle any other unforeseen errors
        return jsonify({"error": {"code": "E003", "message": "An unexpected error occurred.", "details": str(e)}}), 500

@teachers_bp.route('/teachers', methods=['GET'])
def get_teachers():
    """Retrieve all Teachers."""
    try:
        # Query all teacher records
        teachers = Teacher.query.all()
        return jsonify({"teachers": [dict(id=teacher.id, name=teacher.name, email=teacher.email) for teacher in teachers]}), 200

    except Exception as e:
        # Handle any errors during the retrieval process
        return jsonify({"error": {"code": "E003", "message": "An unexpected error occurred while retrieving teachers.", "details": str(e)}}), 500