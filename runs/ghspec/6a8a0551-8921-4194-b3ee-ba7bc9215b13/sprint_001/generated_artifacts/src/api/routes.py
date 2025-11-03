from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from src.services.student_service import StudentService

# Create a new Blueprint for the student management API
student_bp = Blueprint('student', __name__)

# Schema for validating student data
class StudentSchema(Schema):
    name = fields.String(required=True)

# Initialize the student service
student_service = StudentService()

@student_bp.route('/students/', methods=['POST'])
def create_student():
    """Create a new student."""
    json_data = request.get_json()
    # Validate input data
    try:
        data = StudentSchema().load(json_data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": err.messages}}), 400

    # Create student and return the result
    student = student_service.create_student(data['name'])
    return jsonify(student), 201

@student_bp.route('/students/', methods=['GET'])
def get_all_students():
    """Retrieve all students."""
    students = student_service.get_all_students()
    return jsonify(students), 200

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a specific student by ID."""
    student = student_service.get_student(student_id)
    if student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
    return jsonify(student), 200

@student_bp.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student."""
    success = student_service.delete_student(student_id)
    if not success:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404
    return jsonify({"message": "Student deleted successfully"}), 200

# Register the blueprint with the main application
def register_routes(app):
    app.register_blueprint(student_bp)