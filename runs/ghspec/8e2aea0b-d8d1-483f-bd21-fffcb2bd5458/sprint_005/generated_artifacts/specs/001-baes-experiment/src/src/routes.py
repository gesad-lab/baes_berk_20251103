from flask import Blueprint, request, jsonify
from src.models import db, Teacher  # Importing the Teacher model
from src.schemas import TeacherSchema  # Importing the appropriate schema for validation
from flask_sqlalchemy import SQLAlchemy

routes = Blueprint('routes', __name__)

@routes.route('/teachers', methods=['POST'])
def create_teacher():
    """
    Create a new teacher.
    
    Request Body:
    {
        "name": "string",
        "email": "string"
    }

    Response:
    - 201 Created on success with details of the created teacher
    - 400 Bad Request on validation errors
    """
    # Validate and deserialize input data
    schema = TeacherSchema()
    try:
        teacher_data = schema.load(request.json)
    except Exception as e:
        # Return error response for validation issues
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Invalid input data.",
                "details": str(e)
            }
        }), 400

    # Create a new Teacher instance
    new_teacher = Teacher(name=teacher_data['name'], email=teacher_data['email'])
    
    try:
        db.session.add(new_teacher)
        db.session.commit()
    except Exception as e:
        # Rollback the session in case of failure
        db.session.rollback()
        # Log the error and return an internal error response
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Failed to create teacher.",
                "details": str(e)
            }
        }), 500

    # On success, return the created teacher information
    return jsonify({
        "message": "Teacher successfully created.",
        "teacher_id": new_teacher.id,
        "name": new_teacher.name,
        "email": new_teacher.email
    }), 201


@routes.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """
    Retrieve a teacher's information by their ID.

    Response:
    - 200 OK with teacher details if found
    - 404 Not Found if the teacher does not exist
    """
    teacher = Teacher.query.get(teacher_id)
    
    if teacher is None:
        return jsonify({
            "error": {
                "code": "E003",
                "message": "Teacher not found."
            }
        }), 404

    return jsonify({
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    }), 200