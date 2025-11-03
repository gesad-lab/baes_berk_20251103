from flask import Blueprint, request, jsonify
from models.teacher import Teacher
from app import db

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers', methods=['POST'])
def create_teacher():
    """
    Create a new teacher in the database.

    Request Body:
    - name (string): The name of the teacher (required)
    - email (string): The email of the teacher (required)

    Returns:
    - 201 Created with teacher details if successful
    - 400 Bad Request if name or email is missing
    """
    data = request.get_json()

    # Validate request data
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        # Return structured error message if required fields are missing
        return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400

    # Create and save the new teacher
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)

    try:
        db.session.commit()
    except Exception as e:
        # Rollback the session in case of an error during commit
        db.session.rollback()
        # Log the exception in production to help with debugging (not exposing details to user)
        app.logger.error(f"Failed to create teacher: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "Failed to create teacher due to server error."}}), 500

    # Return the details of the created teacher
    return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201