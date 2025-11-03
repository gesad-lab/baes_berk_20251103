from flask import Blueprint, jsonify, request
from src.controllers.student_controller import create_student, get_students, update_student, delete_student

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['POST'])
def add_student():
    """Endpoint for adding a new student."""
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400

    result = create_student(name)
    return jsonify({"message": "Student created successfully.", "student": result}), 201

@student_bp.route('/students', methods=['GET'])
def list_students():
    """Endpoint for retrieving the list of students."""
    students = get_students()
    return jsonify(students), 200

@student_bp.route('/students/<int:student_id>', methods=['PUT'])
def modify_student(student_id):
    """Endpoint for updating a student's name."""
    data = request.json
    new_name = data.get('name')
    
    if not new_name:
        return jsonify({"error": {"code": "E001", "message": "Name field is required."}}), 400

    updated_student = update_student(student_id, new_name)
    
    if updated_student is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    return jsonify({"message": "Student updated successfully.", "student": updated_student}), 200

@student_bp.route('/students/<int:student_id>', methods=['DELETE'])
def remove_student(student_id):
    """Endpoint for deleting a student."""
    result = delete_student(student_id)

    if result is None:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    return jsonify({"message": "Student deleted successfully."}), 200