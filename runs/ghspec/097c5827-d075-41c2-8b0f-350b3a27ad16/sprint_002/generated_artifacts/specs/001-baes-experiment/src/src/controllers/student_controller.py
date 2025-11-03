from flask import Blueprint, request, jsonify
from src.services.student_service import create_student, get_student
from src.models import Student

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['POST'])
def create_student_route():
    """Endpoint to create a new student record.

    Expects a JSON body with an 'email' field.

    Returns:
        JSON response with the created student's data or error message.
    """
    data = request.json

    # Validate input data
    if not data or 'email' not in data:
        return jsonify({"error": {"code": "E001", "message": "Missing 'email' field."}}), 400

    try:
        student = create_student(data['email'])
        return jsonify({"id": student.id, "email": student.email}), 201
    except Exception as e:
        # Log the error (considering logging has been set up in the project)
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 500

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student_route(student_id):
    """Endpoint to retrieve a student record by ID.

    Returns:
        JSON response with the student's data or error message.
    """
    try:
        student = get_student(student_id)
        if student:
            return jsonify({"id": student.id, "email": student.email}), 200
        else:
            return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404
    except Exception as e:
        # Log the error (considering logging has been set up in the project)
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 500